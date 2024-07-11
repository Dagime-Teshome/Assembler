


def print_final_grades(grades):
    total_sum=0;
    for i in range(len(grades)):
        for j in range(1,5):
            total_sum += grades[i][j];
    print(str(total_sum) + " Total Average = "+str(total_sum/len(grades)));
    
grades = [ ['Jane Sammy', 80, 93, 84, 87],
           ['Karyn Small', 97, 98, 91, 92],
           ['Steve Carrol', 87, 75, 73, 81],
           ['Brady Richards', 70, 81, 91, 92]]

print_final_grades(grades);