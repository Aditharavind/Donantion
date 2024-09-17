from django.shortcuts import render, redirect
from .models import Item, Institution, Sponsorship, Chat
from django.contrib.auth.models import User

# View to list all available donation items
def available_items(request):
    items = Item.objects.all()
    institutions = Institution.objects.all()  # Educational institutions, orphanages, old age homes
    context = {
        'items': items,
        'institutions': institutions,
    }
    return render(request, 'donationapp/available_items.html', context)

# Handle sponsorship action
def sponsor_item(request, item_id, institution_id):
    item = Item.objects.get(id=item_id)
    institution = Institution.objects.get(id=institution_id)
    sponsor = request.user
    Sponsorship.objects.create(item=item, institution=institution, sponsor=sponsor)
    return redirect('available_items')

# Chat feature
def chat_with_institution(request, institution_id):
    institution = Institution.objects.get(id=institution_id)
    if request.method == 'POST':
        message = request.POST.get('message')
        Chat.objects.create(institution=institution, user=request.user, message=message)
        return redirect('available_items')

    return render(request, 'donationapp/chat.html', {'institution': institution})
