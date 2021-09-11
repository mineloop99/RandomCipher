#EnterDecrypted Message
Decrypted_Message = "thvvwcztq! cz wecq yiaqq, lfn jcii ivahz wev dcppvhvzyv mvwjvvz vzyhlowcfz azd anwevzwcyawcfz. wecq rvqqatv cq vzyhlowvd jcwe a bvhl czqvynhv vzyhlowcfz qyevrv. cdvaiil, az vzyhlowcfz qyevrv qefnid aiifj fzil anwefhcgvd oahwcvq, jef xzfj wev xvl, wf hvad wev rvqqatv. efjvbvh, lfn snqw hvad wev rvqqatv jcwefnw xzfjczt wev xvl. evzyv, wev vzyhlowcfz qyevrv cq czqvynhv"
print("Decrypted Message:\n", Decrypted_Message)
#Declare Variables
stored_find_c = ['']*100 #Contain all letters have been Replaced
stored_replace_c = ['']*100 #Contain all letters to be Replaced
attempt = Decrypted_Message #Temporary Message used to decrypt
find_c = '\0' #Letter Input
replace_c = '\0' #Letter replacex`
count = 0 #Count Letter has been use
#Use For Loop To Check and replace
for i in range(10000):
    find_c = input("-----------------------------------------\nPlease input letter to find. If you want to undo please Press (back): ")
    if not find_c.isalpha():
        print("\nPlease Enter True word")
        i -= 1
        continue
    if find_c == 'exit':
        break
    if find_c == 'back' and count > 0:
        count -= 1
        attempt = attempt.replace("%s" %stored_replace_c[count].upper(),"%s" %stored_find_c[count])
        i -= 1
        print("You have undo succeed:\n", attempt)
        print("Undo %s with %s \nChanged Number: %s\nLetters:\n%s\nto\n%s\n\n" %(stored_replace_c[count].upper(),stored_find_c[                     count], count, stored_find_c[0:count],stored_replace_c[0:count]))
        stored_find_c[count] = ''
    elif len(find_c) == 1 and not find_c in stored_find_c:
        replace_c = input("Please input letter to replace: ")
        stored_find_c[count] = find_c
        stored_replace_c[count] = replace_c
        attempt = attempt.replace(stored_find_c[count], "%s" %stored_replace_c[count].upper())
        print("You have Replaced succeed:\n",attempt,"\nExit press (exit)")
        print("Replace: %s with %s\nChanged Number: %s\nLetters:\n%s\nto\n%s\n\n" %(stored_find_c[count], stored_replace_c[count].upper(), count+1,stored_find_c[0:count+1],stored_replace_c[0:count+1]))
        count += 1
    else:
        print("\nNot exist or Have been Replaced")