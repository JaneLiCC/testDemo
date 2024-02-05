
import sys
import os
 
# 终止程序的函数
def termProgram():
    # 调用系统退出函数
    sys.exit()


''' 1 SU: 512 NIC, 8 leaf '''
print('''
           This is a topology generation test program which will generate a 2-layer fat-tree topology file. 
           Leaf/spine switches are Spectrum-4, and servers are DGX with 8 Bluefield-3.
           Server and leaf are connected using rail-optimize, which means 8 Bluefield-3 of a DGX connect 8 leafs seperately. 
           The upstream and downstream ports on the leaf layer is 1:1.        
           ''')

# name=input("1. Pleae input the topology name: ")
# dgxCount=int(input("2. Pleae input the number of the DGX(1-64): "))
name = "test"
dgxCount=4
if(dgxCount<1 or dgxCount>64):
    print("DGX number %d is invalid" % (dgxCount))
    termProgram()
leafCount=8
if dgxCount>32 :
    spineCount=4
else: 
    spineCount=2 



#file
# 获取当前工作目录
# current_dir = os.getcwd()
current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

print(name+".dot", dgxCount, leafCount, spineCount, current_dir)
# 要生成的文件名及路径（相对于当前工作目录）
file_name = name+".dot"
file_path = os.path.join(current_dir, file_name)
 
try:
    # 打开或创建文件
    with open(file_path, 'w') as f:
        # 向文件写入内容
        f.write("graph \""+name+"\" {\n")

        #Server
        for i in range(1, dgxCount+1):
            f.write("  \"server%02d\" [ memory=\"1024\" os=\"generic/ubuntu2204\" cpu=\"1\"]\n" % (i))        
        #leaf
        for i in range(1, leafCount+1):
            f.write("  \"leaf%02d\" [ memory=\"2048\" os=\"cumulus-vx-5.7.0\" cpu=\"1\"]\n" % (i))        
        #Spine
        for i in range(1, spineCount+1):
            f.write("  \"spine%02d\" [ memory=\"2048\" os=\"cumulus-vx-5.7.0\" cpu=\"1\"]\n" % (i))  
        #netq
        f.write("  \"netq-ts\" [os=\"netq-ts-cloud-4.5.0\"]\n")    

        # connection: server--leaf
        i=1
        j=0
        for sev in range(1, dgxCount+1):
            for port in range(1, 9):
                f.write("    \"server%02d\":\"eth%d\" -- \"leaf%02d\":\"swp%ds%d\"\n" % (sev, port, port, i, j))
            j=1-j
            if(j==0):
                i=i+1                  

        # connection: leaf--spine
        sep=(dgxCount+spineCount-1)//spineCount  #ceil(dgxCount/spineCount)
        m=1
        for sev in range(1, leafCount+1):
            # f.write(str(m)+"---\n")
            i=33
            j=0
            k=1            
            n=0
            r=m
            for port in range(1, dgxCount+1):
                f.write("    \"leaf%02d\":\"swp%ds%d\" -- \"spine%02d\":\"swp%ds%d\"\n" % (sev, i, j, k, m, n))
                j=1-j
                if(j==0):
                    i=i+1 
                n=1-n;
                
                if(port%sep==0):
                    k=k+1 
                    m=r
                    n=0
                elif(n==0):
                    m=m+1
            
            m=r+(sep+1)//2

        f.write("}")
        f.close()
    print("Done")
except Exception as e:
    print("Exception", str(e))






