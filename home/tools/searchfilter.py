from email import message
from django.http import HttpResponse, request, JsonResponse
from home.models import PublicPost, ShelterAddress
import json

def searchFilter(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        pincode = data['pincode']
        page = int(data['page'])
        if(not pincode.isdigit()):
            # return 400 status code with a message 
            print("pincode is not a digit", pincode)
            return HttpResponse("Pincode should be a number", status=400)

        try:
            post = PublicPost.objects.filter(shelteraddress__pincode=pincode)[(page-1) * 4: page*4]
            allpost = [] 
            for obj in post:
                other_image1 = obj.other_image1.url if obj.other_image1 else None
                other_image2 = obj.other_image2.url if obj.other_image2 else None
                other_image3 = obj.other_image3.url if obj.other_image3 else None

                address = ShelterAddress.objects.get(post_id = obj)
                
                allpost.append([
                    obj.title,
                    obj.id,
                    obj.price,
                    obj.description,
                    address.landmark,
                    address.street,
                    address.pincode,
                    obj.image.url,
                ])
            print('allpost', allpost)
            return JsonResponse(allpost, safe=False)
        except Exception as e:
            print(e)
            return HttpResponse(status=500)
    return HttpResponse("nothing here")