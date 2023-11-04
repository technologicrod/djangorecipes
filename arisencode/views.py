from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home(request):
    all_items = Profile.objects.all()
    context = {'all_items': all_items}
    return render(request, 'home.html', context)
#for logging out
def logout(request):
    request.session.clear()
    return redirect('home')

#for creating profile account
def create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            
            # Check if a user with the same email already exists
            existing_user = Profile.objects.filter(email=email).first()
            
            if existing_user:
                # User with the same email already exists
                context = {"form": form, "error_message": "A user with this email already exists."}
                return render(request, 'create.html', context)
            else:
                # User doesn't exist, save the new user
                form.save()
                return redirect('home')
        else:
            context = {"form": form}
            return render(request, 'create.html', context)
    else:
        form = ProfileForm()
        context = {"form": form}
        return render(request, 'create.html', context)

#for dashboard for both admin and basic users    
def dashboard(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            # Manually check if the email and password match a profile
            profiles = Profile.objects.all()
            for profile in profiles:
                if profile.email == email and profile.password == password:
                    request.session['email'] = email
                    request.session['id'] = profile.id
                    request.session['account_type'] = profile.account_type
                    recipes = Recipe.objects.filter(user=profile.id)
                    context = {"user_email": request.session['email'], "account_type": profile.account_type, "id": request.session['id'], "recipes": recipes}
                    return render(request, 'dashboard.html', context)
            # If no matching profile is found, handle authentication failure
            error_message = "Invalid email or password"
            return redirect('home')
        else:
            error_message = "Form not valid."
            return redirect('home')
    if 'email' in request.session:
        email = request.session['email']
        profile_id = request.session['id']
        recipes = Recipe.objects.filter(user=profile_id)
        context = {
            "user_email": email,
            "account_type": Profile.objects.get(id=profile_id).account_type,
            "id": profile_id,
            "recipes": recipes
        }
        return render(request, 'dashboard.html', context)
    else:
        # Handle the case when the user is not authenticated (no session data)
        return redirect('home')

#for adding recipe    
def addrecipe(request):
    context = {"user_email": request.session['email']}
    context['form'] = RecipeForm()
    return render(request, 'addrecipe.html', context)

#for editing recipe
def editrecipe(request, id):
    print(f"Editing recipe with ID: {id}")
    
    try:
        # Retrieve the specific recipe based on the 'id' parameter
        recipe = Recipe.objects.get(id=id)
        
        if request.method == 'POST':
            form = RecipeForm(request.POST, instance=recipe)
            if form.is_valid():
                form.save()
                print(f"Recipe updated: {recipe.name}")
                return redirect('dashboard')
        else:
            print(request.method)
            form = RecipeForm(instance=recipe)

        context = {
            "user_email": request.session['email'],
            "form": form,
            "id": id
        }

        return render(request, 'editrecipe.html', context)
    except Recipe.DoesNotExist:
        print(f"Recipe with ID {id} does not exist")
        # Handle the case when the recipe with the given ID does not exist

#for deleting recipe but not actually deleting it, only changing the status from 'Active' to 'Inactive'
def inactiverecipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.status = "Inactive"
    recipe.save()
    return redirect('dashboard')

#for admin deleting recipe
def inactiverecipeadmin(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.status = "Inactive"
    recipe.save()
    return redirect('admindb')

#for creating a recipe
def saverecipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        user_id = request.session.get('id')
        form.instance.user_id = user_id
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            error_message = "Form not valid."
            context = {"user_email": request.session['email']}
            return render(request, 'addrecipe.html', context)
    else:
        form = RecipeForm()
        context = {"form": form}
        return render(request, 'dashboard.html', context)

#for admin dashboard, accessing all recipes
def admindb(request):
    if 'email' in request.session:
        recipes = Recipe.objects.all()
        context = {
            "user_email": request.session['email'],
            "account_type": request.session['account_type'],
            "recipes": recipes,
        }
        return render(request, 'admindb.html', context)
    else:
        # Handle the case when the user is not authenticated (no session data)
        return redirect('home')