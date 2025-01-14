def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        # Start each row with 1
        new_row = [1]
        
        # Calculate the middle values
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        
        # End each row with 1
        new_row.append(1)
        triangle.append(new_row)

    return triangle

