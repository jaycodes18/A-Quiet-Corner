# A-Quiet-Corner

It is a digital diary that mimics a physical notebook where people record their daily life experiences and emotions which they can look back to. I built a digital version of that, and my aim was to match the aesthetics of a real book and make it feel like a safe place for the users to express their feelings.

## Preview

![Closed diary cover](https://cdn.discordapp.com/attachments/1517653758970953850/1517788290848133221/image.png?ex=6a378dff&is=6a363c7f&hm=8846f0f169311e71735a172d848faced2b0a6a41610d950250d1d0576e2997ca)
![Open diary cover](https://cdn.discordapp.com/attachments/1517653758970953850/1517784378468597812/image.png?ex=6a378a5a&is=6a3638da&hm=e87bb43d9e84f6ffe4dc2be39c7e2814b119e0b8bd8a025feb9f486fed25d3c9)
## How to use it

Open the link to the website in a browser, and record your daily experiences in the date accordingly, and you can look back on your writings as time goes on.

## Features

- Digital diary
- Aesthetics of a real diary (book like cover and lined pages, as well the page turning animations)
- Two page spread with live date and day
- Autosave while typing (when run locally), you can look back at your writing

## Limitations/ Things to work on for the future

Currently, it doesn't save the thing that you write in the diary. When you refresh the page, the content goes away. That's a serious limitation because people usually tend to close the tab once they're done writing, so it would be better if it saved.
Initially it saved locally and I could view what I was writing in a json file, and it also saved when I refreshed (I was on localhost), but I had to remove it because I can't deploy with that on vercel.

## Coding Languages

- Frontend: HTML, CSS, Javascript
- Backend: Python (flask)
- Deployed on Vercel

## Link to access the website

https://a-quiet-corner-f5db.vercel.app

## AI Usage

- Debugging: I used AI to debug my code as it had many issues, especially in flask (python) as I'm fairly new working with it
- Writing code in Flask: I haven't really used flask before, I knew python, so I used ai to figure out how to use flask to make the backend work.
- Deployment: I used AI to deploy my website on vercel, I used to use netlify if it was only a single HTML file, but now since I have flask, I had to figure out how to deploy it.
  I added these files: requirements.txt and vercel.json based on the instructions from coding assistant, and it enabled me to successfully deploy this website.
- Some Technical stuff: like how to mimic the book opening and page turning animation, and things related to that.
