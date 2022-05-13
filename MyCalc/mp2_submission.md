<table><tr><td> <em>Assignment: </em> Mini Project 2_Advanced Calculator</td></tr>
<tr><td> <em>Student: </em> Abzal Rahima Kowsar Mohammad(am3355)</td></tr>
<tr><td> <em>Generated: </em> 5/13/2022 7:36:06 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-2_advanced-calculator/grade/am3355" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Prepare your workspace</p>
<ol>
<li><code>git checkout dev</code></li>
<li><code>git pull origin dev</code></li>
<li><code>git checkout -b MP2-AdvCalc</code></li>
</ol>
<p>In this project, you&#39;ll decorate or extend one of the given MyCalc samples (do not edit MyCalc directly).
For every added calculation you&#39;ll need to provide a positive and negative test case.
<strong>Note:</strong> negative test cases will throw and capture exceptions to generate a positive test case
Negative test cases test for invalid input and/or invalid operations. These test cases will be via csv files as well 
(just like the changes to addition, subtraction, multiplication, division, square, and square root)</p>
<p>HINT 1: You can generate a normal distribution of random distribution of numbers with excel to use for your data:  Here (<a href="http://howtoexcel.org/statistics/normal-distribution/">http://howtoexcel.org/statistics/normal-distribution/</a>)</p>
<p>HINT 2: You can create another excel file that contains the answers to your calculations that you can use in your unit tests.</p>
<p><strong>Your program needs to additionally calculate the following:</strong></p>
<ol>
<li>Square</li>
<li>Square Root</li>
<li>Pick 5 from below<ul>
<li>Population Mean</li>
<li>Median</li>
<li>Mode</li>
<li>Population Standard Deviation</li>
<li>Variance of population proportion</li>
<li>Z-Score</li>
<li>Standardized score</li>
<li>Population Correlation Coefficient</li>
<li>Confidence Interval</li>
<li>Population Variance</li>
<li>P Value</li>
<li>Proportion</li>
<li>Sample Mean</li>
<li>Sample Standard Deviation</li>
<li>Variance of sample proportion</li>
</ul>
</li>
</ol>
<ul>
<li>You&#39;ll update your previous test cases to read from csv files for the input and output values.</li>
<li>Use the below csv files for your existing test cases of addition, subtraction, multiplication, and division.
As well as testing the new square and square root modifications.</li>
</ul>
<p><strong>Note</strong>: You may need to view the data via the &quot;Raw&quot; button on the gist.
<a href="https://gist.github.com/MattToegel/958ad17cc2c94337a5260126639eefbe">https://gist.github.com/MattToegel/958ad17cc2c94337a5260126639eefbe</a> </p>
<p>Once done do the following:</p>
<ol>
<li>Git add all changes (including the test case csv files)</li>
<li>Git commit with relevant messages</li>
<li>Git push origin MP2-AdvCalc</li>
<li>Create a Pull Request on Github to dev (keep it open)</li>
<li>Fill out the details here</li>
<li>Save and Generate the markdown (any changes require this step to be repeated)</li>
<li>Paste the content into a <code>mp2_submission.md</code> file</li>
<li>Git add/commit/push the submission file change</li>
<li>Complete the pull request merge</li>
<li>Create a new pull request from dev to prod and complete it</li>
<li>Navigate to prod branch&#39;s <code>mp2_submission.md</code> file and paste the direct link to Canvas</li>
</ol>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Added Functionality: Square </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168194910-a89673e5-9987-44d7-b438-b3fff711c241.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this screenshot I am doing the function for squaring of a number<br>by importing static method<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the passing test cases from the csv file</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Added Functionality: Square Root </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168194969-0f2c3e75-fd4c-4c16-beb1-b7af7ff6ef97.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this screenshot I am doing the function for squareroot of a number<br>by importing static method<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the passing test cases from the csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168196476-16c46954-28a3-4582-856d-fab9691f48d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test case<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Choice 1 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>in here i am taking mean function as my choice, it is useful<br>to<br>find the mean of dataset mostly the industry will be helpful with<br>this function<br>it<br>just find the mean point in a set of numbers</p><br><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168195007-be29d3a5-7207-44ac-8409-aece0f9d1790.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this screenshot I am doing the function for mean of a number<br>by importing static method<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168196556-5443e884-3322-490b-b85b-cfdd260bb65f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test case of sqrt<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of negative test case execution</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Choice 2 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>in here i am taking median function as my choice, it is useful<br>to<br>find the median of dataset mostly the industry will be helpful with<br>this function<br>it<br>just find the median point in a set of numbers</p><br><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168195070-b3ef1a4f-725d-4bf3-9abe-1fa8b0fdfa13.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this screenshot I am doing the function for median of a number<br>by importing static method<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168196646-b6a8901b-6ea0-46d7-bdca-88ca044fa58a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>testcase sqrt<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of negative test case execution</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Choice 3 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>in here i am taking mode function as my choice, it is useful<br>to<br>find the mode of dataset mostly the industry will be helpful with<br>this function<br>it<br>just find the mode in a set of numbers<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168195147-f4637cd8-b5d2-4d4b-8e3f-5c1ff530e3be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this screenshot I am doing the function for mode of a number<br>by importing static method<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168196719-f3b6e1e3-b359-43a8-8568-a94449c5238b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test case of mean<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of negative test case execution</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Choice 4 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>(missing)</p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168195220-d29b4411-1419-4b87-8f82-838e0ed0f67e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>in here i am using the standard deviation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168196865-d47951dd-5a75-49da-8a5a-f8dd7b6e3c2d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test case of mode<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Choice 5 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>in here i am using the standard deviation function in here which is<br>been used as the function of the choice .<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168196040-a88ef817-6d36-4a9a-8b44-5b3733629ffe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>standard deviation function is used in here<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98247151/168196801-dc38455e-8921-4787-a7fd-f4111f1769ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>standard deviation testcase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Mention any difficulties and how you overcame them or what you learned during this mini project.</td></tr>
<tr><td> <em>Response:</em> <p>the difficulties i am facing is that i am not able to perform<br>operations<br>on the csv files. I need the knowledge in that</p><br><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Pull Request Link(s) for this project</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/am3355/IS-601004/pull/16">https://github.com/am3355/IS-601004/pull/16</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-2_advanced-calculator/grade/am3355" target="_blank">Grading</a></td></tr></table>
