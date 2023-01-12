

from rest_framework.views import APIView, Response, status
from api.models import Zodiac, Ratio

class ZodiacView(APIView):
    
    def post(self, request):

        content = {}

        z1 = request.data.get('zodiac1')
        z2 = request.data.get('zodiac2')
        n1 = request.data.get('name1')
        n2 = request.data.get('name2')
        
        try:
            zodiac1 = Zodiac.objects.get(name=z1)
            zodiac2 = Zodiac.objects.get(name=z2)

            try:
                ratio = Ratio.objects.get(zodiac1=zodiac1, zodiac2=zodiac2)
            except:
                ratio = Ratio.objects.get(zodiac1=zodiac2, zodiac2=zodiac1)
            
            content['ratio'] = ratio.ratio
            content['desc'] = f'{n1} ve {n2} arasındaki uyum yüzde {int(ratio.ratio*100)}'

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(content, status=status.HTTP_200_OK)