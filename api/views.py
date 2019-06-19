import json
import pandas as pd
import dask.dataframe as dd

from django.conf import settings

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class BikeRental(APIView):
    """
       BikeRental http get method read the hour.csc file and it's calculated the standard deviation of 
       registred and casual user on week day bases.

        Endpoints : /api/v1/bike-rentals/
        method: GET

       it's return the json response.
        {
            "message": "The standard deviation of week day.",
            "status": 200,
            "data": {
                "registered": {
                    "Monday": 105.9728992768,
                    "Tuesday": 159.5178967701,
                    "Wednesday": 170.1032453495,
                    "Thursday": 172.3447516018,
                    "Friday": 169.3273948092
                },
                "casual": {
                    "Monday": 68.0906625104,
                    "Tuesday": 35.097055953,
                    "Wednesday": 26.1708945447,
                    "Thursday": 27.7906575322,
                    "Friday": 27.7680884927
                }
            }
        }
    """
    
    def get(self, request, format=None):
        

        file = '{0}/{1}'.format(settings.BASE_DIR, 'hour.csv')

        day_of_Week= {
                        0:'Monday', 
                        1:'Tuesday', 
                        2:'Wednesday', 
                        3:'Thursday', 
                        4:'Friday', 
                        5:'Saturday', 
                        6:'Sunday'
                    }
        
        dd_df = dd.read_csv(file)
        # convert dask dataframe to pandas dataframe.
        df = dd_df.compute()

        # calculate the standard deviation of registred and casual user group by week days.
        df = df[~df['weekday'].isin([5,6])].groupby(
                        df['weekday'])['registered','casual'].std()

        # replace index number to index name
        df.index = df.index.map(day_of_Week)

        return Response({
                'message': 'The standard deviation of week day.',
                'status': status.HTTP_200_OK,
                'data': json.loads(df.to_json())
            })
