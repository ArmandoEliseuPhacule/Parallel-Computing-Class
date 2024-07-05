### Important Notes ###

The class exam given on 04/07/2024 is submitted as following: 

1. Armando Eliseu Phacule ---> Exam.docx + Exam_scenarios.docx

2. Luan Pachisso ---> LuanExam.docx 
   
3. António Andre Junior ---> was unwell and missed the exam.

Documentation for both assignments is as following:

Assigment 1
1. powerpoint presentation ---> Parallel-Supermarket-Checkout-Simulation.pptx
2. word document ---> Parallel_Computing_Assigment_1_Documentation.docx
   
Assigment 2
1. powerpoint presentation ---> Assignment_Two.pptx
2. word document ---> Parallel_Computing_Assignment2.docx

The source code for our assignment1 can be ran through ---> main.py

The main.py code was optimized by implementing several key improvements to enhance performance, reliability, and resource management. A multiprocessing Lock was introduced to synchronize console output, preventing race conditions and ensuring sequential printing. The individual Process creations were replaced with a more efficient multiprocessing Pool, which manages worker processes and provides automatic load balancing across CPU cores. The three separate cashier functions were consolidated into a single, parameterized function, improving code maintainability. The use of Pool.starmap enables parallel execution of tasks, making better use of available system resources. Memory efficiency was improved through the Pool's automatic process management, and the overall code structure was reorganized for better readability and encapsulation. These changes collectively result in a more scalable, efficient, and robust implementation of the checkout system simulation, while maintaining the original functionality and logic.

changes visible in ---> mainUpdate.py
