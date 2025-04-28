 def calculate_area_perimeter(length, width):
       """Calculates both the area and perimeter of a rectangle."""
       area = length * width
       perimeter = 2 * (length + width)
       return f"Area: {area}, Perimeter: {perimeter}"

   if __name__ == "__main__":
       result = calculate_area_perimeter(5, 3)
       print(result)