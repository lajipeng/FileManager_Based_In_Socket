
#输入账号和密码

def encryption():

    # import dnn

    import time

    init_usrname= "admin"

    init_password= "admin"

    flag0=0

    flag1=0

    print('>>>User Login<<<')

    while True:

        usr=input('   enter username:    ')

        if usr==init_usrname:

            while flag0<3:

                password= B()

                print(password)

                if password==init_password:

                    print()

                    print("+++++++++++++++++++++++++")

                    print('     Success Login!')

                    print("+++++++++++++++++++++++++")

                    print()

                    time.sleep(1)

                    flag1=1

                    break

                else:

                    flag0 +=1

                    if flag0<=2:

                       print('Wrong Password,enter again!')

            if flag1==1:

                 break

            flag0=0

            print ('You have tried three times,login again!')

        else:

            print ('Wrong Username,enter again!')

'''

    Python3的字符串的编码语言用的是unicode编码，由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干字节，如果要在网络上传输，或保存在磁盘上就需要把str变成以字节为单位的bytes

python对bytes类型的数据用带b前缀的单引号或双引号表示：



                  'ABC'



                  b'ABC'



要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显得和前者一样，但bytes的每个字符都只占用一个字节

'''

 

#密码星号打印

def B():

    import msvcrt, os

    print('   enter password:    ', end='', flush=True)

    li = []

    while 1:

        ch = msvcrt.getch()

        #回车

        if ch == b'\r':

            return b''.join(li).decode() #把list转换为字符串返回

            break

        #退格

        elif ch == b'\x08':

            if li:

                li.pop()

                msvcrt.putch(b'\b')

                msvcrt.putch(b' ')

                msvcrt.putch(b'\b')

        #Esc

        elif ch == b'\x1b':

            break

        else:

            li.append(ch)

            msvcrt.putch(b'*')

    return b''.join(li).decode()

    #os.system('pause')

 

#测试

if __name__ == '__main__':

    encryption()
