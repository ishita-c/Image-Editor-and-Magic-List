# Image-Editor-and-Magic-List
Link to <a href="https://github.com/ishita-c/Image-Editor-and-Magic-List/tree/master/Problem%20Statement">problem statement and expected outputs</a>.
# Image Editor
This python script can perform following tasks on a pgm (portable graymap format) by reading the image in the form of an array:
* Average_pgm: acts as an averaging filter and blurs the image by assigning the pixel value equal to average of neighbouring pixels.
* Edge_pgm: detects the edges by calculating gradient of pixels, normalization of pixels and wrapping for boundary conditions are also used.
* Energy_pgm: finds the minimum energy path by implementing an algorithm that finds a path from top of the image to the bottom. The path is highlighted with white colour.
 
  Test image with results can be viewed in testimg-image-editor folder.
# Magic List
Implementation of data structure with following functions:
* Find_min: returns the minimum element of magic list.
* Insert: inserts a new element at appropriate place so that the conditions of magic list are satisfied.
* Delete_min: deletes the min element, and returns modified list.
* K_sum: returns the sum of minimum K elements of the list.

