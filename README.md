<table><tr><td> <em>Assignment: </em> Mini Project 3 - Flask AdvCalc</td></tr>
<tr><td> <em>Student: </em> Abzal Rahima Kowsar Mohammad(am3355)</td></tr>
<tr><td> <em>Generated: </em> 5/13/2022 9:07:57 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-3---flask-advcalc/grade/am3355" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol>
<li>Create a new branch called MP3-Flask-AdvCalc</li>
<li>Add the ability to load a basic csv file of mixed sets of data/equations for add/sub/div/mult</li>
<li>Add UI support for your 5 stats functions from MP2 (buttons on the screen that trigger the equation) The user should be able to enter data and run each of your stats functions as expected</li>
<li>Add the ability to load an advanced csv file of fixed data/equations for the 5 stats functions (or load in 5 different files separately)</li>
<li>Give the ability for the user to delete a single history item of theirs</li>
<li>Give the ability for the user to delete all of their history (this should not affect any other user&#39;s history)</li>
<li>Add test cases to <ol>
<li>Register a user</li>
<li>Login the user</li>
<li>To run a calc function for the user and record/create a SimpleHistory (verify this gets created with proper data)</li>
<li>Make sure the User and SimpleHistory data get deleted after the test phase</li>
</ol>
</li>
<li>Fill in the below deliverables (make sure screenshots load properly)</li>
<li>Create an mp3_submission.md file in your project/app folder</li>
<li>Paste the generated markdown into this file</li>
<li>git add/commit/push to MP3-Flask-AdvCalc</li>
<li>Merge to dev</li>
<li>Merge dev to prod</li>
<li>Find the mp3_submission.md in the prod branch on github</li>
<li>Submit the direct link to that file to Canvas</li>
</ol>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Basic CSV Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the mixed csv data of add/sub/mult/div</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168202214-db905c94-3649-4e83-a9a9-5ca1f8a104b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot is showing CSV file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the history after uploading the csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168202589-2377ef05-81fe-4a06-8f79-34f0a1bba370.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img src="https://user-images.githubusercontent.com/98247151/168202799-90e12533-5efd-48c7-b60c-217ad95ca695.png" alt="image"><br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how the csv is processed and the data is sent to the calculator</td></tr>
<tr><td> <em>Response:</em> <p>In calc folder(views.py) a decorator called my calc.route is created with upload_csv function.<br>This<br>route is working for uploading the CSV, the first file is uploaded<br>if it<br>works it is printed the uploaded file passes information to work<br>in the original<br>working MyCalc.py and gives the result<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Adv Calc Functions </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the new Advanced buttons on the UI</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168203019-8fa2250f-83c6-484b-9443-ecfd65ca224b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The above screenshot is showing advanced buttons of SMean, SMode, SMedian, Sqrt, Square,<br>Variance, sstd_dev<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the aggregated history of each 5 advanced function being ran</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168203379-29f8a4a0-926e-4127-91b7-662526af3935.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>History after uploading the CSV file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain how you updated the calculator to handle the advanced function interaction</td></tr>
<tr><td> <em>Response:</em> <p>In view.py the decorator mycalc. route with function upload_csv(): is working for<br>advanced CSV<br>file. For my project same route is working for both advance<br>and simple functions<br>of uploading CSV. The original MyCalc.py in the calc<br>folder is doing a collection<br>of nums(in_nums) then it pops out the first<br>row with(mean, median, mode) and then<br>calculates the for a remaining list and<br>gives the result.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Advanced CSV Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of mixed advanced csv data (or separate csv files if you wish)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168204492-62c025f8-14bf-4b68-b670-6e5e8ddf8780.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the csv file of advance functions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the aggregated history the csv file execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168204791-a323a84e-fbd7-4724-8783-40c2108fa3bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this is the result in apprun in terminal<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain how you updated the calculator to handle the advanced function interaction</td></tr>
<tr><td> <em>Response:</em> <p>MyClac.py does all the calculations, views.py is handling those calculations logic for reading<br>and<br>processing information from websites and mycalc.html does the design of the page.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> History Management </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of deleting a single history item</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168205057-7c03e7ff-db49-4cc7-bcb1-90e6473589be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the screen shot before deleting single history. I will delete first<br>history from here.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot showing the history being cleared (all of it for this user)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168205344-83a2187f-b6d0-4b72-985a-40c3cf017b0a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the history being cleared all of it.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show that the history is still present for other users (that task 2 didn't delete it for other users)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168205534-d2fd7b49-cc83-43f1-b3f7-d3224945eb5c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing that the history is still present for other users<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain how you implemented single delete of the history</td></tr>
<tr><td> <em>Response:</em> <p>For deleting history also need to create a route, also have to<br>pass in<br>a specific blog post id so we know which one to<br>delete. then created<br>functiuon called (delete_single_history) passed id, and look<br>into in database and grab that id<br>and we can delete it.. So<br>after grabbing the single id no that is<br>passed when we click the<br>delete button<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain how you implemented deleting all of the logged in user's history</td></tr>
<tr><td> <em>Response:</em> <p>For deleting the whole history, again need to create a route, first<br>history is<br>collected and a history id is needed. Also, have to<br>pass in the post<br>id so we know which one to delete. then<br>created function called (def delete():<br>passed id, and look into<br>in database and grab that id and we can<br>delete it.. So after<br>grabbing the single id no that is passed when we<br>click the delete<br>button.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot the test case code to register a test user via pytest</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168206230-fc12dea5-3b5e-40db-b0f8-04aa878bcb0e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the test case code to register a test user via pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot the passing test case from pytest for task 1</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168206303-3240c188-ecf6-4084-9c34-77c5cad8c6ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the passing test case from pytest for task1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot the test case code for logging in the test user via pytest</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot the passing test case from pytest for task 3</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshot the test case code for recording a SimpleHistory for the test user (should be a valid generation from the calculator)</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshot the passing test case from pytest for task 5</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain the flow/process of these new test cases that pass the test user around</td></tr>
<tr><td> <em>Response:</em> <p>The process of the new test cases is to check if each module<br>is<br>working properly or not,I have not done testcases for all of the<br>tasks.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add a link to your deployed app </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/ff0000/000000?text=Incomplete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add the link here to the hosted instance</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-3---flask-advcalc/grade/am3355" target="_blank">Grading</a></td></tr></table>
