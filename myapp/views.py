from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import Student,UserProgress,UserProfile,Badge,UserBadge
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.messages import get_messages

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['cpass']
        avatar = request.FILES.get('avatar')
        level=0
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Is Already in USed')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username ALready exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username , email=email , password=password)
                user_profile = UserProfile(user=user)

                if avatar:
                    user_profile.avatar = avatar
                user_profile.save()
                user.save()
                return redirect('login')
        else:
            messages.info(request,"password Mismatch")
            return redirect('register')
    else:
        return render(request,'SignUp.html')

def intro_page(request):
    return render(request,'Intro.html')


def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('intro2')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')
    
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
@login_required
def intro2(request):
    return render(request,'intro2.html')
@login_required


def courses(request):
    try:
        progress = UserProgress.objects.get(user=request.user)
        total_courses = 4
        completed_courses = sum([getattr(progress, f'course{i}_completed') for i in range(1, total_courses + 1)])  
    except UserProgress.DoesNotExist:
        # If the UserProgress object doesn't exist for the user, set completed_courses to 0.
        completed_courses = 0

    return render(request, 'courses.html', {'completed_courses': completed_courses})
def C11(request):
    if request.method == 'POST':
        user = request.user
        try:
            progress = UserProgress.objects.get(user=user)
            if progress.completed_chapters == 0:
                progress.completed_chapters += 1
                progress.save()
            else :
                 pass
        except UserProgress.DoesNotExist:
            UserProgress.objects.create(user=user, completed_chapters=1)
        return redirect('C12')  # Replace 'C12' with the URL name for the next chapter (C12)
    return render(request,'C11.html')
def C12(request):
    if request.method == 'POST':
        user = request.user
        try:
            progress = UserProgress.objects.get(user=user)
            if progress.completed_chapters == 1:
                progress.completed_chapters += 1
                progress.save()
            else :
                 pass
        except UserProgress.DoesNotExist:
            UserProgress.objects.create(user=user, completed_chapters=1)
        return redirect('C13')  # Replace 'C12' with the URL name for the next chapter (C12)
    return render(request,'C12.html')
def C13(request):
    if request.method == 'POST':
        badge = Badge.objects.get(name='AI Novice Badge')
        user = request.user
        try:
            progress = UserProgress.objects.get(user=user)
            if progress.completed_chapters == 2:
                progress.completed_chapters += 1
                progress.course1_completed = True
                progress.save()
                if not UserBadge.objects.filter(user=user, badge=badge).exists():
                    UserBadge.objects.create(user=request.user, badge=badge)
                    messages.success(request, f'Congratulations! You have completed this chapter and earned the "{badge.name}" badge!')
            else:
                pass
        except UserProgress.DoesNotExist:
            UserProgress.objects.create(user=user, completed_chapters=1, course1_completed=False)
        return redirect('C2')  # Replace 'C2' with the URL name for the next chapter

    return render(request, 'C13.html')




def C21(request):
    if request.method == 'POST':
        return redirect('C22')
    return render(request,'C21.html')
def chapter_completed(request, chapter_number):
    user_progress, created = UserProgress.objects.get_or_create(user=request.user)
    if not created:
        user_progress.completed_chapters = chapter_number
        user_progress.save()
    return redirect('courses')

def Profile(request):
    user = request.user
    progress = UserProgress.objects.get(user=user)

    total_courses = 4  # replace with the actual total number of courses
    completed_courses = sum([getattr(progress, f'course{i}_completed') for i in range(1, total_courses + 1)])  
    completed_percentage = (completed_courses / total_courses) * 100
    completed_percentage = round((completed_courses / total_courses) * 100)  # rounding off to the nearest integer
    completed_percentage_str = f'{completed_percentage}%'
    if completed_percentage < 33:
        color = 'red'
    elif completed_percentage < 66:
        color = 'yellow'
    else:
        color = 'green'
    return render(request, 'profile.html', {'progress': progress, 'completed_percentage': completed_percentage_str,'color': color})
   
def C22(request):
    if request.method == 'POST':
        user = request.user
        try:
            progress = UserProgress.objects.get(user=user)
            if progress.completed_chapters_course2 == 0:
                progress.completed_chapters_course2 += 1
                progress.save()
            else :
                 pass
        except UserProgress.DoesNotExist:
            UserProgress.objects.create(user=user, completed_chapters_course2=1)
        return redirect('C22a')  # Replace 'C12' with the URL name for the next chapter (C12)
    return render(request,'C22.html')


def C22a(request):
    if request.method == 'POST':
        user = request.user
        try:
            progress = UserProgress.objects.get(user=user)
            if progress.completed_chapters_course2 == 1:
                progress.completed_chapters_course2 += 1
                progress.save()
            else :
                 pass
        except UserProgress.DoesNotExist:
            UserProgress.objects.create(user=user, completed_chapters_course2=1)
        return redirect('C23')  # Replace 'C12' with the URL name for the next chapter (C12)
    return render(request,'C22a.html')

def C23(request):
    if request.method == 'POST':
        badge = Badge.objects.get(name='AI Problem Solver')
        user = request.user
        try:
            progress = UserProgress.objects.get(user=user)
            if progress.completed_chapters_course2 == 2:
                progress.completed_chapters_course2 += 1
                progress.course2_completed = True
                progress.save()
                if not UserBadge.objects.filter(user=user, badge=badge).exists():
                    UserBadge.objects.create(user=request.user, badge=badge)
                    messages.success(request, f'Congratulations! You have completed this chapter and earned the "{badge.name}" badge!')
            else:
                pass
        except UserProgress.DoesNotExist:
            UserProgress.objects.create(user=user, completed_chapters_course2=1, course2_completed=False)

        return redirect('C3')  # Replace 'C2' with the URL name for the next chapter

    return render(request, 'C23.html')


def C31(request):
    if request.method == 'POST':
        user = request.user
        try:
            progress = UserProgress.objects.get(user=user)
            if progress.completed_chapters_course3 == 0:
                progress.completed_chapters_course3 += 1
                progress.save()
            else :
                 pass
        except UserProgress.DoesNotExist:
            UserProgress.objects.create(user=user, completed_chapters_course3=1)
        return redirect('C32')  # Replace 'C12' with the URL name for the next chapter (C12)
    return render(request,'C31.html')

def C32(request):
    if request.method == 'POST':
        badge = Badge.objects.get(name='AI Wizard')
        user = request.user
        try:
            progress = UserProgress.objects.get(user=user)
            if progress.completed_chapters_course3 == 1:
                progress.completed_chapters_course3 += 1
                progress.course3_completed = True
                progress.save()
                if not UserBadge.objects.filter(user=user, badge=badge).exists():
                    UserBadge.objects.create(user=request.user, badge=badge)
                    messages.success(request, f'Congratulations! You have completed this chapter and earned the "{badge.name}" badge!')
            else:
                pass
        except UserProgress.DoesNotExist:
            UserProgress.objects.create(user=user, completed_chapters_course3=1, course3_completed=False)
        return redirect('C4')  # Replace 'C2' with the URL name for the next chapter
    return render(request, 'C32.html')

def C41(request):
    if request.method == 'POST':
        user = request.user
        try:
            progress = UserProgress.objects.get(user=user)
            if progress.completed_chapters_course4 == 0:
                progress.completed_chapters_course4 += 1
                progress.save()
            else :
                 pass
        except UserProgress.DoesNotExist:
            UserProgress.objects.create(user=user, completed_chapters_course4=1)
        return redirect('C42')  # Replace 'C12' with the URL name for the next chapter (C12)
    return render(request,'C41.html')

def C42(request):
    if request.method == 'POST':
        badge = Badge.objects.get(name='AI Wizard')
        user = request.user
        try:
            progress = UserProgress.objects.get(user=user)
            if progress.completed_chapters_course4 == 1:
                progress.completed_chapters_course4 += 1
                progress.course4_completed = True
                progress.save()
                if not UserBadge.objects.filter(user=user, badge=badge).exists():
                    UserBadge.objects.create(user=request.user, badge=badge)
                    messages.success(request, f'Congratulations! You have completed this chapter and earned the "{badge.name}" badge!')
            else:
                pass
        except UserProgress.DoesNotExist:
            UserProgress.objects.create(user=user, completed_chapters_course4=1, course4_completed=False)
        return redirect('courses')  # Replace 'C2' with the URL name for the next chapter
    return render(request, 'C42.html')

def C1(request):
    return render(request,'C1.html')

def C2(request):
    return render(request,'C2.html')

def C3(request):
    return render(request,'C3.html')

def C4(request):
    return render(request,'C4.html')