# Python_Basics
Learning Python basics

<details>
<summary>decorator</summary>
  
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
> ```
> deco함수는 데코레이터 함수로, 인자로 함수이름을 받음.
>
> def test(x,y) 에서, test를 정의할때 데코함수 deco가 먼저 실행됨.
> 이때 deco는 11을 출력하고, 내부함수 _deco를 정의하고 22를 출력함.
> 이후 내부함수 _deco를 리턴하면서 test(10,20)를 실행함, 이때 33을 출력.
> 그후 test에서 44를 출력. 이후 test(30,40)을 실행.
> decorator함수인 deco는 test를 정의할때 한번 실행되므로, 11 22는 한번 출력이되고,
> test는 _deco를 먼저 실행하므로 33후 test에서 44를 출력하는것임. 
>
> 상기할점은, 데코레이터함수(deco)는 내부함수(_deco)를 정의하기 위해 단 한번 @deco에서 실행이되고, 
> 그 이후 deco된 함수(test)가 실행될때는 내부함수만 실행되는것임.
> ```

</details>

<details>
<summary>defaultdict</summary>

> ``` 
> defaultdict는 매우 간단함.
> 기존의 dict는 key가 존재하는지 체크해주어야 하는데, defaultdict는 key가 없더라도 value값을 설정해줌.
> 
> 예를 들어, list의 요소가 key, 요소들의 출현횟수를 value로 갖는 dict를 선언할때, defaultdict로 선언 할 수 있음.
> 이 때 defaultdict 의 value값을 명시해줄수있는데, int로 선언해줌.
> ```
> 
> defaultdict.py
> ```python
> from collections import defaultdict
> 
> numbers=[1,4,5,1,3,10,8,4,1,1]
> numbers_defaultdict=defaultdict(int)
> 
> for i in numbers:
>     numbers_defaultdict[i]+=1
> 
> print(numbers_defaultdict)
> ```
> 
> 위 코드의 출력결과는 
> 
> ```python
> defaultdict(<class 'int'>, {1: 4, 4: 2, 5: 1, 3: 1, 10: 1, 8: 1})
> ```

</details>

<details>

<summary>function parameter</summary>

> function_parameters.py
> ```python
> 
> '''
> From a function's perspective:
> 
> A parameter is the variable listed inside the parentheses in the function definition.
> 
> An argument is the value that is sent to the function when it is called.
> '''
> 
> #function with two parameters
> def foo1(name1, name2):
>     print(name1, name2)
> 
> #function with three parameters
> def foo2(name1, name2, name3):
>     print(name1, name2, name3)
> 
> #function with one parameter, and one default parameter
> #non-default arguments cannot appear after default arguments
> def foo3(name1, name2='Dragonite'):
>     print(name1, name2)
> 
> #function with non-keyword arguments
> #args will be tuple
> def foo4(*args):
>     print(args)
> 
> #function with keyword arguments
> #kwargs will be dict
> def foo5(**kwargs):
>     print(kwargs)
> 
> 
> #call with positional arguments
> foo1('Jigglypuff','Dragonite')
> 
> #call with keyword arguments
> foo2(name2='Ditto', name3='Jigglypuff', name1='Lapras')
> 
> #call with mixing positional arguments & keyword arguments
> #positional arguments cannot appear after keyword arguments
> foo2('Ditto', name3='Lapras', name2='Mew')
> 
> #call with only one argument
> foo3('Jigglypuff')
> 
> #call with arbitrary number of arguments
> foo4('Mew', 'Ditto', 'Lapras', ('Plusle','Minun'))
> 
> #call with arbitrary number of arguments, each argument's types are key=value
> foo5(name1='Mew', name2='Ditto', name3='Lapras', name4='Snorlax')
> ```
> 
> ```
> 함수를 호출할때, positional arguments, keyword arguments 구분을 잘 해야함.
> positional argument 는 keyword argument 다음에 나올 수 없음.
> *args, **kwargs 의 리턴값은 각각 튜플, 딕셔너리임.
> ```
>
> 출력결과
> 
> ```
> 
> Jigglypuff Dragonite
> Lapras Ditto Jigglypuff
> Ditto Mew Lapras
> Jigglypuff Dragonite
> ('Mew', 'Ditto', 'Lapras', ('Plusle', 'Minun'))
> {'name1': 'Mew', 'name2': 'Ditto', 'name3': 'Lapras', 'name4': 'Snorlax'}
> 
> ```






</details>
