# Python_Basics
Learning Python basics

<details>
<summary>Decorator</summary>
  
> deco.py 
>   
> ```python
> def deco(func_name):
>     print(11)
>     def _deco(*args, **kwargs):
>         print(33)
>         result = func_name(*args, **kwargs)
>         return result
>     print(22)
>     return _deco
> 
> @deco
> def test(x,y):
>     print(44)
>     return x+y
> 
> test(10,20)
> test(30,40)
> ```
> 위의 deco.py를 실행시킬경우, 결과는 아래와 같이 나옴. 
>   
> ```
> 11
> 22
> 33
> 44
> 33
> 44
> ```
> 
> deco함수는 데코레이터 함수로, 인자로 함수이름을 받음.
> 
> def test(x,y) 에서, test를 정의할때 데코함수 deco가 먼저 실행됨.
> 
> 이때 deco는 11을 출력하고, 내부함수 _deco를 정의하고 22를 출력함.
> 
> 이후 내부함수 _deco를 리턴하면서 test(10,20)를 실행함, 이때 33을 출력.
> 
> 그후 test에서 44를 출력. 이후 test(30,40)을 실행.
> 
> decorator함수인 deco는 test를 정의할때 한번 실행되므로, 11 22는 한번 출력이되고,
> test는 _deco를 먼저 실행하므로 33후 test에서 44를 출력하는것임.
> 
> 상기할점은, 데코레이터함수(deco)는 내부함수(_deco)를 정의하기 위해 단 한번 @deco에서 실행이되고, 
> 그 이후 deco된 함수(test)가 실행될때는 내부함수만 실행되는것임.

</details>
