# Receipt Line Isolation
[ ] Identify the left-hand alignment of the text
[ ] Identify the right-hand alignment of the text
[ ] parse the full text for all $number.number sets (aka prices)
[ ] for each price, determine if the price is right-aligned (a total) or left aligned (a price with a quantity i.e. 5 @ $3.00)
[ ] Find the set of left-most words across all lines of text
[ ] identify line-pairs (each receipt item can span one or two lines)
[ ] combine line1+line2 to get full product names (remove any leading decimals which would be product numbers)
[ ] for each product name, identify the corresponding right-aligned price (aka total)
[ ] create a CSV with each product name and the total
[ ] create a UI to properly stack the images by hand rather than hard-coded image rotations
[ ] lower the resolution on the images so they aren't so large when talking to Google Vision API


----

Switching gears
- https://kivy.org/doc/stable/guide/widgets.html
- Kivy program needs to display a single image
- Kivy needs to display two images
- Kivy needs to let you select an image to display
- Kivy needs to let you add an image
