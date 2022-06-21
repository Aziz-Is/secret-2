from django.shortcuts import render

# Create your views here.


def show_numbers(request):
    if request.method == "GET":
        return render(request, 'input_html.html')
    elif request.method == "POST":
        secret_nums = [5, 1, 2, 9]
        print(request.POST)
        res = request.POST.get("numbers")
        print("RES", res)
        result = res.split(' ')
        list_of_numbers = [int(x) for x in result]
        print(list_of_numbers)
        bulls = 0
        cows = 0
        for i in range(len(list_of_numbers)):
            if list_of_numbers[i] == secret_nums[i]:
                bulls += 1
            elif list_of_numbers[i] in secret_nums:
                cows += 1

        return render(request, 'result.html', {'bulls': bulls, 'cows': cows})