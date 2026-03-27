def main():
  row_to_check = [{2, 3, 4, 5}, {1, 2, 3, 4}, {1, 2, 3, 4}, {2, 3, 4}, {8}, {7}, {6}, {1}]
  row_to_check_with_visisble_skyscraper_numbers = [{5}, {2, 3, 4, 5}, {2, 3, 4}, {2, 3, 4}, {2, 3, 4}, {8}, {7}, {6}, {1}, {1}]
  real_to_check_with_visisble_skyscraper_numbers = [{5}, {2, 3, 4, 5}, {2, 3, 4}, {2, 3, 4}, {2, 3, 4}, {8}, {7}, {6}, {1}, {1}]
  if len(row_to_check_with_visisble_skyscraper_numbers[0]) == 1:
    visisble_skyscraper_number = next(iter(row_to_check_with_visisble_skyscraper_numbers[0]))
  else:
    visisble_skyscraper_number = 0
  if visisble_skyscraper_number > 1 and visisble_skyscraper_number < 8 - 1:
    biggest_smallest_number = 0
    visible_skycrapers = 0
    highest_building_value = 0
    indexes_biggest_numbers = []
    num_empty_squares = 0
    numbers_before_biggest_smallest_number = []
    for counter in range(0, 8):
      if {8-counter} in row_to_check:
        biggest_smallest_number = 8-counter
        indexes_biggest_numbers.append(row_to_check.index({8-counter})+1)
      else:
        break
    if biggest_smallest_number > 0:
      minimum_index_of_biggest_numbers = min(indexes_biggest_numbers)
      for index in range(2, 9):
        if index < minimum_index_of_biggest_numbers:
          if len(row_to_check_with_visisble_skyscraper_numbers[index]) == 1:
            numbers_before_biggest_smallest_number.append(next(iter(row_to_check_with_visisble_skyscraper_numbers[index])))
        else:
          if next(iter(row_to_check_with_visisble_skyscraper_numbers[index])) > highest_building_value:
            highest_building_value = next(iter(row_to_check_with_visisble_skyscraper_numbers[index]))
            visible_skycrapers += 1
          if len(row_to_check_with_visisble_skyscraper_numbers[index]) > 1:
            num_empty_squares += 1
      if visible_skycrapers == visisble_skyscraper_number - 1:
        real_to_check_with_visisble_skyscraper_numbers[1].clear()
        for counter in range(0, num_empty_squares + 1):
          if len(row_to_check_with_visisble_skyscraper_numbers[1]) > 0:
            value_to_add = max(row_to_check_with_visisble_skyscraper_numbers[1])
          row_to_check_with_visisble_skyscraper_numbers[1].discard(value_to_add)
          real_to_check_with_visisble_skyscraper_numbers[1].add(value_to_add)
        if len(numbers_before_biggest_smallest_number):
          max_number_before_biggest_smallest_number = max(numbers_before_biggest_smallest_number)
          for value_to_remove in range(1, max_number_before_biggest_smallest_number + 1):
            real_to_check_with_visisble_skyscraper_numbers[1].discard(value_to_remove)
        if not real_to_check_with_visisble_skyscraper_numbers[1]:
          return False
      elif visible_skycrapers < visisble_skyscraper_number - 1 and visisble_skyscraper_number != 2 and visible_skycrapers != len(indexes_biggest_numbers):
        for counter in range(1, visisble_skyscraper_number - visible_skycrapers):
          for num in range(counter, visisble_skyscraper_number - visible_skycrapers):
            value_to_remove = biggest_smallest_number - (visisble_skyscraper_number - visible_skycrapers - num)
            real_to_check_with_visisble_skyscraper_numbers[counter].discard(value_to_remove)
          if not real_to_check_with_visisble_skyscraper_numbers[counter]:
            return False
  print(real_to_check_with_visisble_skyscraper_numbers)


main()

            
            