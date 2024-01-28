# Gestura

## Inspiration
We wanted to select facial recognition but it is already a very advanced and developed upon. This led us to gesture recognition and using it help people with special needs. Since, humanity has now moved to space, we have people from different cultural backgrounds and languages living in a community together. The WHO estimates that 466 million people were living with disability hearing impairment in 2018 and this number is supposed to be doubled by 2025. This is where gesture recognition makes it easy to communicate especially for people with special needs as it allows to talk seamlessly without lesser problems. This is how we ended up on the idea to create an ASL Gesture recognition software.

## What it does
The software takes in ASL gestures and converts them to English alphabets thus forming words. These words are displayed on the screen as text and the text on the screen is spoken after that. The users have an option to select a language from English, French, Spanish, Japanese and Chinese to convert the ASL gesture to and for it to spoken in that language. We have another bonus feature that lets us communicate with new species since humans are now in space. It takes in gestures for the language and converts it to English making it very feasible to talk to these newfound species. It also converts text in English to 3D animated gestures of these species. 

## How we built it
**Machine Learning for ASL Recognition**
In the first phase of our project we delved into machine learning to develop a robust system for converting American sign language asl gestures into text we created our own dataset containing hand gestures we trained our model to recognize and classify each frame of sign language into its corresponding letter by utilizing machine learning algorithms using TensorFlow and keras to implement a CNN like model our system became adept at understanding the intricacies and variations in hand movements providing accurate and efficient conversion from sign language to text.

**Computer Vision for Gesture Recognition**
To enhance the user experience we implemented computer vision techniques to recognize and interpret hand gestures in Realtime using OpenCV our system can detect the position movement and orientation of hands allowing for gesture recognition.

**Full Stack Web Development**
After successfully implementing machine learning and computer vision we incorporated to the side of full stack web development to make our solution user-friendly by allowing not techsavy people to use the program we created a user-friendly website that allows the use of the sign language translation service offering an intuitive interface for users to input gestures and receive corresponding text and speech outputs we used JS, HTML, CSS along with node.js and express for our server side to create this interface.

**Unity Animation for Alien Modelling**
In the final phase we incorporated unity a powerful game development engine to bring an interactive d model to life we designed an animated alien character that mirrors the sign language gestures for alien language being input into the system this not only adds a visually engaging element to the website but also serves as a dynamic tool for users to visually confirm the accuracy of their sign language input the unity animation provides an immersive experience.

## Challenges we ran into
- We struggled to find a suitable data set of ASL gestures on which to train an accurate model. Due to this, we created models with high variance and low bias leading to inaccurate and finicky results.
- We could not find an premade Unity aminations for the movements we required for our 3D model of an alien, so we had to manually animate the model.
- We had to switch from a client-side tech stack to a server-side tech stack for building the website to integrate Python scripting directly into the website.
- We initially had a lot of scattered streams of functionalities being developed for our project. It was tough to combine them holistically into one fully functional website.

## Accomplishments that we're proud of
- We managed to complete the project with almost no prior knowledge of the tech stack we ended up using.
- We substantially increased the accuracy and reliability of our trained model after several iterations of data recording and editing within just a matter of a few hours.
- We integrated autocorrect, translation, and text-to-speech algorithms in our program to increase accessibility for our users.

## What we learned
- We explored 3D modelling in Unity and animation using skeleton rigging
- We learn how to use OpenCV and TensorFlow to train our model and generate hand recognition.
- We learned how to run a Python script through a JS environment using Node.js

## What's next for Gestura
- Support for translation in more languages.
- Hosting this software on a public-access platform.
- Increasing the epoch batch size and sample size during our model training process for a more reliable model.
