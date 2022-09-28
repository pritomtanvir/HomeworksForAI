
# coding: utf-8

# In[1]:

from math import e, log


# In[2]:

#input_raw = "P (0,2,1) (2,0,-1) (0,4,1) (4,0,-1)"
#input_raw = "L (0,2,1) (2,0,-1) (0,4,-1) (4,0,1) (0,6,-1) (6,0,1)"
#print("Please type in instances")
#print("i.e. P (0,2,1) (2,0,-1) (0,4,1) (4,0,-1)")
#print("i.e. L (0,2,1) (2,0,-1) (0,4,-1) (4,0,1) (0,6,-1) (6,0,1)")
input_raw = input()


# In[3]:

list_raw = input_raw.replace("(", "").replace(")", "").replace(",", " ").split(" ")
list_raw.pop(0)
list_raw = [int(i) for i in list_raw] 
train_data = [list_raw[i * 3 : i * 3 + 3] for i in range(len(list_raw) // 3)] 
train_data


# In[4]:

def perceptron(train_data):
    w1, w2 = 0, 0
    for i in range(100):
        for item in train_data:
            y_raw = item[0] * w1 + item[1] * w2
            if y_raw >= 0:
                y_out = 1
            else:
                y_out = -1
                
            if (item[2] == y_out):
                pass
            else:
                w1 = w1 + item[2] * item[0]
                w2 = w2 + item[2] * item[1]
    print(w1,",", w2)


# In[5]:

def logistic(train_data):
    a, w1, w2 = 0.1, 0, 0
    final_p_list = []
    
    for item in train_data:
        if(item[2] == -1):
            item[2] = 0
            
    for i in range(100):
        for item in train_data:
            z = w1 * item[0] + w2 * item[1]
            p = 1 / (1 + pow(e, -z))
            w1 = w1 + a * item[0] * (item[2] - p)
            w2 = w2 + a * item[1] * (item[2] - p)
    #print(w1, w2)
    
    for item in train_data:
        z = w1 * item[0] + w2 * item[1]
        p = 1 / (1 + pow(e, -z))
        final_p_list.append(p)
    print(final_p_list)


# In[6]:

if "P" in input_raw:
    perceptron(train_data)
elif "L" in input_raw:
    logistic(train_data)
else:
    print("Format error")


# In[ ]:



