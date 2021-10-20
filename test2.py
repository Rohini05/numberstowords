def numberstowords(number):
    units = ("", "one ", "two ", "three ", "four ","five ", "six ", "seven ","eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ", "seventeen ", "eighteen ", "nineteen")
    tens  =("","", "twenty ", "thirty ", "forty ", "fifty ","sixty ","seventy ","eighty ","ninety ")

    if number < 0:
        return "minus "+ numberstowords(-number)

    if number<20:
        return  units[number] 

    if number<100:
        return  tens[number // 10]  + units[int(number % 10)] 

    if number<1000:      
        return units[number // 100]  +"hundred and " +numberstowords(int(number % 100))

    if number<1000000: 
        return  numberstowords(number // 1000) + "thousand " + numberstowords(int(number % 1000))

    if number < 1000000000:    
        return numberstowords(number // 1000000) + "million " + numberstowords(int(number % 1000000))

    return numberstowords(number // 1000000000)+ "billion "+ numberstowords(int(number % 1000000000))

x =int(input("Enter a number:"))
print(numberstowords(x))