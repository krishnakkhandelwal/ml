#!/bin/bash

while true
do
    echo "----- Arithmetic Operations Menu -----"
    echo "1. Addition"
    echo "2. Subtraction"
    echo "3. Multiplication"
    echo "4. Division"
    echo "5. Exit"
    read -p "Enter your choice: " choice

    if [ "$choice" -eq 5 ]; then
        echo "Exiting program."
        break
    fi

    read -p "Enter first number: " num1
    read -p "Enter second number: " num2

    case $choice in
        1) result=$((num1 + num2))
           echo "Result: $result"
           ;;
        2) result=$((num1 - num2))
           echo "Result: $result"
           ;;
        3) result=$((num1 * num2))
           echo "Result: $result"
           ;;
        4) 
           if [ "$num2" -ne 0 ]; then
               result=$(echo "scale=2; $num1 / $num2" | bc)
               echo "Result: $result"
           else
               echo "Error: Division by zero not allowed."
           fi
           ;;
        *) echo "Invalid choice. Please try again." ;;
    esac
    echo
done

