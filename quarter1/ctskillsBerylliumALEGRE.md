# Annex A: Computational Thinking Exercise: "Smart School Canteen Queue"
**Name**: Yzel Alexa Alegre
**Date**: 08/19/26

---
*Scenario*: The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:
- Some students take too long to decide what to order.
- The cashier has to manually calculate totals and give change.
- There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

---
## Step 1: Identify the Big Problem
Main Problem: During specific times, the school canteen experiences long queues, maybe, due to a lack of workers or too many students. This leads to frustration for everyone, students being late to class, and inefficient ordering. The goal of this code is to design a system that helps manage and optimize the ordering and queue process.

## Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:
1. How will the students know the menu for the day, and how can they order before reaching the counter?
2. How will the system prepare the meal based on when they ordered?
3. How will the system validate the payment, and confirm the order?

## Step 3: Apply Computational Thinking Skills
| **Sub-Problem** | **CT Skill** | **Proposed Solution** |
|---|---|---|
| Log-In and Pre-Order | Clarity and focus | Students would use their device to log in and check the menu, then place an order. |
| Queue Management | Efficiency  | The system would give out numbers or tokens to each students and use it to estimate when they will receive their order. There will be a screen that displays the live count. |
| Order and Payment Verification | Foundation for algorithms | It checks the digital balance and generates a validation notification to confirm the order. |

## Step 4: A Pseudocode for the Identified Sub-problems

```text
START
    # Initialize variables
    SET total_queue_count TO 0
    SET estimated_prep_time_per_item TO 2  #in minutes

    WHILE Canteen_Is_Open DO
        IF Student_Places_Order THEN
            READ student_id, item_list, quantity

            #Calculate estimated wait time for this specific order
            SET current_order_item_count TO SUM(quantity)
            SET order_wait_time TO current_order_item_count * estimated_prep_time_per_item

            #Update queue tracking
            SET total_queue_count TO total_queue_count + 1
            SET token_number TO total_queue_count

            # Display order details to student
            PRINT "Order Confirmed!"
            PRINT "Your Token Number is: ", token_number
            PRINT "Estimated Wait Time: ", order_wait_time, " minutes"

            #Send order details to kitchen queue
            SEND_TO_KITCHEN(token_number, item_list)
        ENDIF
    ENDWHILE
END








 




START
    # Initialize variables
    SET total_queue_count TO 0
    SET estimated_prep_time_per_item TO 2  #in minutes

    WHILE Canteen_Is_Open DO
        IF Student_Places_Order THEN
            READ student_id, item_list, quantity

            #Calculate estimated wait time for this specific order
            SET current_order_item_count TO SUM(quantity)
            SET order_wait_time TO current_order_item_count * estimated_prep_time_per_item

            #Update queue tracking
            SET total_queue_count TO total_queue_count + 1
            SET token_number TO total_queue_count

            # Display order details to student
            PRINT "Order Confirmed!"
            PRINT "Your Token Number is: ", token_number
            PRINT "Estimated Wait Time: ", order_wait_time, " minutes"

            #Send order details to kitchen queue
            SEND_TO_KITCHEN(token_number, item_list)
        ENDIF
    ENDWHILE
END

