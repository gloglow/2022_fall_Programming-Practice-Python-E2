import math

input_file='data_q_4.txt'
output_file='corrected_data_q4.txt'
fd=open(input_file, 'r', encoding='utf-8')
fd_out=open(output_file, 'w', encoding='utf-8')
cnt_error=0
cnt_line=1

for line in fd:
    row=line.split()
    x=float(row[0])
    y=float(row[1])
    r=float(row[2])
    indice_error=math.pow((math.cos(x)+y-r),2)
    if indice_error>0.001:
        print("There is error in ",cnt_line,"th row (squared error : ",indice_error,")")
        cnt_error+=1
        r=math.cos(x)+y
    fd_out.write("%.17f %.17f %.17f\n" %(x,y,r))
    cnt_line+=1

print("Total number of detected errors : ",cnt_error)



