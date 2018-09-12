# brother_python_learning
[中文版](README_CN.md) | [English](README.md)

The purpose of writing two versions is to explain to you that the English foundation is also important in programming learning. You should be accustomed to using English to read and write documents.
## overview
Some tasks will be posted from time to time, please note the update. Or if you have any gains and accumulations, you can update this project. I will check them regularly. The learning of programming focuses on turning theory into code, hopes to persist.
## about git
Before you go to the project, you need to have some basic understanding of the version control tool specific git. So I have listed some references below.
1. basic using of git
to reference: 
    [git简明指南](http://rogerdudler.github.io/git-guide/index.zh.html),
    [图解git](http://marklodato.github.io/visual-git-guide/index-zh-cn.html?no-svg#conventions),
    [git Book](https://git-scm.com/book/zh/v2),
    [git 详细操作指南](https://juejin.im/post/58c7a4cf61ff4b005da83c42)

2. How to submit code to other‘s project on github, which is also the way you submit code in this project.

    to reference: 
    [知乎: 如何开始在Github上参与开源项目贡献代码?](https://www.zhihu.com/question/39721968)

## about IDE
The compiler to writing python code is not specified, you can choose it by yourself, you only need to upload your `'.py'` file to the project.
## tasks
1. - [x] Please use python to write a program that print out odd and even numbers which in all natural numbers no larger than 50. The effect is as follow:
    ```
    50以内的奇数和偶数如下：
    0 既不是奇数也不是偶数
    奇数: 1, 3, 5, ... , 49
    偶数: 2, 4, 6, ... , 50
    ```
    * Results  -- Guangbin Zhu
        * C 
        ```C
        #include<stuio>
        void main(){
            int odd_number[30],oushu[30],i,j,k;
            for(i=0,j=0,k=0;i<=50;i++){
                if(i%2==0)
                    oushu[k++]=i;
                else
                    odd_number[j++]=i;
            }
        }
        ```
        ```
        estimate：wrong answer, lack of output process, please modify the code.
        ```
        * python for jupyter
        ```python
        odd_numbers=[]
        oushu=[]
        for i in range(51):
            if (i % 2 == 0):
                oushu.append(i)
            else:
                odd_numbers.append(i)    
        odd_numbers
        oushu
        ```
        ```
        代码输出结果如下：
        [1,3,5,7, 9,11,13,15,17,19,21,23,25,27,29,31,33,37,39,41,43,45,47,49]
        [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50]
        ```
        ```
        estimate: wrong answer, because 0 is not a odd number,nor a even number.
        ```
2. - [ ] Please use python to write a program that implements a 21 x 21 multiplication table, The effect is as follow:
    ```
    1: 1 x 1 = 1
    2: 1 x 2 = 2, 2 x 2 = 4
    3: 1 x 3 = 3, 2 x 3 = 6, 3 x 3 = 9
            ...
            ...
            ...
    21: 1 x 21 = 21, 2 x 21 = 42, 3 x 21 = 63, 4 x 21 = 84, ... , 21 x 21 = 441 
    ```
3. - [ ] Please use python to write a program to print the content of the `print_file.txt` file in this project.
4. - [ ] Please use python to write a program to copy the `print_file.txt` to a new file named `print_file_copy.txt`.
## some attentions
* When writing a program, the name of project、variable in the program, etc. should be as good as possible. Do not take some names such as `abc`, `a`, `123`.
* Beginner period of programming, write more annotated.
* If you don't understand, check the information with internet or ask for me, especially you should be good at consulting the official documents.