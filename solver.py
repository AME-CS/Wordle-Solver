from words import sorted_letter_freq,total_valid_words
import random
def valid_word(word,complete_valid_letters,present_valid_letters,invalid_letters):
    if any((char in invalid_letters) for char in word):return False
    for _,(index,letter) in enumerate(complete_valid_letters.items()):
        if letter.isalpha() and (letter not in word or word[index]!=letter):return False
    for _,(index,letter) in enumerate(present_valid_letters.items()): 
        if letter.isalpha() and (letter not in word or word[index]==letter):return False
    return True
def sorted_guesses(filtered_words):
    word_freq={}
    for _,word in enumerate(filtered_words):
        freq_score=uniqueness_score=0
        letters_in_word=''
        for char in word:
            freq_score+=sorted_letter_freq[char]
            if char not in letters_in_word:
                letters_in_word+=char
                uniqueness_score+=1
        word_freq[word]=(uniqueness_score,freq_score)
    sorted_arr=[]
    for _,(word,_) in enumerate(sorted(word_freq.items(), key=lambda kv: kv[1],reverse=True)):
        sorted_arr.append(word)
    return sorted_arr
invalid_letters=''
present_valid_letters={0:'',1:'',2:'',3:'',4:''}
complete_valid_letters={0:'',1:'',2:'',3:'',4:''}
#driver=webdriver.Chrome()
#filler_letter='x'
#correct_index='#63aa55'
#invalid_letter='#606685'
#incorrect_index='#eab308'
#i=green_counter=row=num_of_success=num_of_success=0
#driver.get(f'https://www.devangthakkar.com/wordle_archive/?1')
#driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div/button').click()
iterations=correct_answers=100000
guess=[]
fails=cout=0
for _ in range(iterations):
    '''
    count+=1
    real_count+=1
    print(real_count)
    if count==228:
        count=0
    i=green_counter=row=guess=0
    wordle_problem=str(count)
    driver.get(f'https://www.devangthakkar.com/wordle_archive/?{wordle_problem}')
    driver.find_element(By.XPATH,'/html').send_keys(filler_letter+random.choice(wordle_list)+Keys.ENTER)
    grid=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div').find_elements(By.TAG_NAME,"span")
    '''
    print(cout)
    invalid_letters=''
    present_valid_letters={0:'',1:'',2:'',3:'',4:''}
    complete_valid_letters={0:'',1:'',2:'',3:'',4:''}
    word=random.choice(total_valid_words)
    guesses=0
    used_letters=''
    curr_word=''
    while curr_word!=word:
        filtered_words=[curr_word for curr_word in total_valid_words if valid_word(curr_word,complete_valid_letters,present_valid_letters,invalid_letters)]
        try:
            curr_word=random.choice(filtered_words)
            guesses+=1
        except:
            print("lol u fukd up")
            break
        for i,letter in enumerate(curr_word):
            if letter in word and letter!=word[i]:
                present_valid_letters[i]=letter
                used_letters+=letter
            elif (letter in word) and (letter==word[i]):
                present_valid_letters[i]=''
                complete_valid_letters[i]=letter
                used_letters+=letter
            elif letter not in word:
                present_valid_letters[i]=''
                invalid_letters+=letter
                used_letters+=letter
        if curr_word==word and guesses>6:
            correct_answers-=1
    print(used_letters)
    guess.append(guesses)
    cout+=1
percentage_of_successes="{:.2%}".format(correct_answers/iterations)
average_num_of_guesses=sum(guess)/len(guess)
dc={}
for i in range(1,35):
    dc[i]=0
for i,v in enumerate(guess):
    dc[v]+=1
print(dc)
print(percentage_of_successes)
print("The number of correct answers found is "+ str(correct_answers))
print(f"There were {iterations-correct_answers} failures")
print(average_num_of_guesses)
print(str(percentage_of_successes)+" Success Rate")

     

'''
for curr_grid in grid:
        curr_letter=curr_grid.text.lower()
        color = Color.from_string(curr_grid.value_of_css_property('background-color')).hex
        if color==invalid_letter:
            invalid_letters+=curr_letter
        elif color==incorrect_index:
            present_valid_letters[i]=curr_letter
        elif color==correct_index:
            complete_valid_letters[i]=curr_letter
        if complete_valid_letters[i].isalpha():
            green_counter+=1
        if color!=incorrect_index:
            present_valid_letters[i]=''
        i+=1
        if i == 5 and green_counter!=5:
            filtered_words=[curr_word for curr_word in total_valid_words if valid_word(curr_word,complete_valid_letters,present_valid_letters,invalid_letters)]
            guess+=1
            try:
                top_guess=filtered_words[0]
            except:
                guesses.append(guess)
                break
            driver.find_element(By.XPATH,'/html').send_keys(filler_letter+top_guess+Keys.ENTER)
            time.sleep(5)
            i=green_counter=0
        elif green_counter==5:
            num_of_success+=1
            guess+=1
            guesses.append(guess)
            break
toast = ToastNotifier()
average_num_of_guesses=sum(guesses)/len(guesses)
percentage_of_successes="{:.2%}".format(num_of_success/iterations)
toast.show_toast(title="Wordle Solver Results",msg=f"Average # of guesses: {average_num_of_guesses}"+"\nSuccess Rate: "+str(percentage_of_successes),duration=1)
print("The number of correct answers found is "+ str(num_of_success))
print(f"There were {iterations-num_of_success} failures")
print(average_num_of_guesses)
print(str(percentage_of_successes)+" Success Rate")
#want letter freq at each letter
''''''arr=[]
for letter in string.ascii_lowercase:
    letter_freq_index=[(0,0),(1,0),(2,0),(3,0),(4,0)]
    for word in total_valid_words:
        for i,char in enumerate(word):
            if char==letter:
                temp=letter_freq_index[i][1]
                letter_freq_index.pop(i)
                temp+=1
                letter_freq_index.insert(i,(i,temp))
    arr.append((letter,letter_freq_index))
for dic in arr:
    for _,(index,freq) in enumerate(dic):
        a.append()
num=[(0,0),(0,0),(0,0),(0,0),(0,0)]
for index,(letter,freqs) in enumerate(arr):
    for j,(char_index,freq) in enumerate(freqs):
        if freq>num[char_index][1]:
            num[char_index]=(letter,freq)
print(num)
'''

    

 

    
'''optimal_starting_word='soare'
invalid_letters=''
present_valid_letters={0:'',1:'',2:'',3:'',4:''}
complete_valid_letters={0:'',1:'',2:'',3:'',4:''}
#to do: *modify logic to deal w a letter in present or complete valid letters that is now an invalid choice
#*structure code look better less scripty more proey
#*need better way of prioritizing guesses its bad rn
def valid_word(word,complete_valid_letters,present_valid_letters,invalid_letters):
    if any((char in invalid_letters) for char in word):return False
    for _,(index,letter) in enumerate(complete_valid_letters.items()):
        if letter.isalpha() and (letter not in word or word[index]!=letter):return False
    for _,(index,letter) in enumerate(present_valid_letters.items()): 
        if letter.isalpha() and (letter not in word or word[index]==letter):return False
    return True

def sorted_guesses(filtered_words):
    word_freq={}
    for _,word in enumerate(filtered_words):
        freq_score=uniqueness_score=0
        letters_in_word=''
        for char in word:
            freq_score+=sorted_letter_freq[char]
            if char not in letters_in_word:
                letters_in_word+=char
                uniqueness_score+=1
        word_freq[word]=(uniqueness_score,freq_score)
    sorted_tup=sorted(word_freq.items(), key=lambda kv: kv[1],reverse=True)
    return f"'{sorted_tup[0][0]}'\n{len(sorted_tup)}"
filtered_words=[curr_word for curr_word in wordle_list if valid_word(curr_word,complete_valid_letters,present_valid_letters,invalid_letters)]
#print(sorted_guesses(filtered_words))
'''
    
""" 
def filter_unwanted_chars(invalid_letters,curr_word):
    if len(invalid_letters)<=0:return True
    for letter in invalid_letters:
        if letter in curr_word:return False
    return True 
"""        

"""  
def complete_valid_pos(valid_letters,curr_word):
    if len(valid_letters)<=0:return True
    for index in valid_letters:
        letter=valid_letters[index]
        if letter.isalpha() and (letter not in curr_word or curr_word[index]!=letter):return False
    return True 
"""
'''
letter_freq={}
for word in total_valid_words:
    for letter in word:
        if letter in letter_freq:
            letter_freq[letter]+=1
        else:
            letter_freq[letter]=1
sorted_letter_freq=sorted(letter_freq.items(), key=lambda kv: kv[1],reverse=True)
print(sorted_letter_freq)
sorted_freq_dict={}
for _,(char,freq) in enumerate(sorted_letter_freq):
    sorted_freq_dict[char]=freq
print(sorted_freq_dict)
#for key, value in sorted(letter_freq.items(), key=lambda kv: kv[1], reverse=True):
    #print("%s: %s" % (key, value))
#cross validate output with total word freq and letter uniqueness
'''
