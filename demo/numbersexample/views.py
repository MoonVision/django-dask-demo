from dask import delayed
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from daskmanager.daskmanager import DaskManager
from daskmanager.serializers import DaskTaskSerializer
from numbersexample.models import Number
from numbersexample.serializers import NumberSerializer


class NumberViewSet(viewsets.ModelViewSet):
    serializer_class = NumberSerializer
    queryset = Number.objects.all()

    @action(['get'], detail=False)
    def square_sum(self, request, pk=None):
        # Get objects from database
        numbers = list(Number.objects.all().values_list('value', flat=True))

        # Build graph
        squares = []
        for number in numbers:
            number_squared = delayed(lambda n: n**2)(number)
            squares.append(number_squared)
        sum_squares = delayed(sum)(squares)

        # Submit graph to Dask
        dask_task = DaskManager().compute(sum_squares)

        # Return task
        return Response(DaskTaskSerializer(instance=dask_task, context=self.get_serializer_context()).data)
