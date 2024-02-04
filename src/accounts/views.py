# accounts/views.py
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def signup(request):
    #HTTP 요청이 POST 방식일 때 실행
    if request.method == 'POST':
        #사용자가 입력한 비밀번호와 비밀번호 확인 값이 일치하는지 확인
        if request.POST['password1'] == request.POST['password2']:
            #create_user() 함수를 이용해 새로운 유저 객체를 생성합니다. username, password, email 필드를 입력
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            #user 객체로 로그인
            auth.login(request, user)
            #회원가입이 성공적으로 처리되었다면, '/'(홈) 페이지로 이동
            return redirect('/')
        #회원가입이 실패한 경우, 다시 회원가입 페이지
        return render(request, 'signup.html')
    return render(request, 'signup.html')