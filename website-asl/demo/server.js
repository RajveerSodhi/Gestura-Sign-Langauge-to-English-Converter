const express = require("express");
const path = require("path");
const { exec } = require("child_process");
const translatte = require("translatte");

const app = express();
const port = process.env.PORT || 3000;
    const langs = {
      "afrikaans": "af",
      "albanian": "sq",
      "amharic": "am",
      "arabic": "ar",
      "armenian": "hy",
      "azerbaijani": "az",
      "basque": "eu",
      "belarusian": "be",
      "bengali": "bn",
      "bosnian": "bs",
      "bulgarian": "bg",
      "catalan": "ca",
      "cebuano": "ceb",
      "chichewa": "ny",
      "chinese (simplified)": "zh",
      "chinese (traditional)": "zh-tw",
      "corsican": "co",
      "croatian": "hr",
      "czech": "cs",
      "danish": "da",
      "dutch": "nl",
      "english": "en",
      "esperanto": "eo",
      "estonian": "et",
      "filipino": "tl",
      "finnish": "fi",
      "french": "fr",
      "frisian": "fy",
      "galician": "gl",
      "georgian": "ka",
      "german": "de",
      "greek": "el",
      "gujarati": "gu",
      "haitian creole": "ht",
      "hausa": "ha",
      "hawaiian": "haw",
      "hebrew": "he",
      "hindi": "hi",
      "hmong": "hmn",
      "hungarian": "hu",
      "icelandic": "is",
      "igbo": "ig",
      "indonesian": "id",
      "irish": "ga",
      "italian": "it",
      "japanese": "ja",
      "javanese": "jw",
      "kannada": "kn",
      "kazakh": "kk",
      "khmer": "km",
      "korean": "ko",
      "kurdish (kurmanji)": "ku",
      "kyrgyz": "ky",
      "lao": "lo",
      "latin": "la",
      "latvian": "lv",
      "lithuanian": "lt",
      "luxembourgish": "lb",
      "macedonian": "mk",
      "malagasy": "mg",
      "malay": "ms",
      "malayalam": "ml",
      "maltese": "mt",
      "maori": "mi",
      "marathi": "mr",
      "mongolian": "mn",
      "myanmar (burmese)": "my",
      "nepali": "ne",
      "norwegian": "no",
      "pashto": "ps",
      "persian": "fa",
      "polish": "pl",
      "portuguese": "pt",
      "punjabi": "pa",
      "romanian": "ro",
      "russian": "ru",
      "samoan": "sm",
      "scots gaelic": "gd",
      "serbian": "sr",
      "sesotho": "st",
      "shona": "sn",
      "sindhi": "sd",
      "sinhala": "si",
      "slovak": "sk",
      "slovenian": "sl",
      "somali": "so",
      "spanish": "es",
      "sundanese": "su",
      "swahili": "sw",
      "swedish": "sv",
      "tajik": "tg",
      "tamil": "ta",
      "telugu": "te",
      "thai": "th",
      "turkish": "tr",
      "ukrainian": "uk",
      "urdu": "ur",
      "uzbek": "uz",
      "vietnamese": "vi",
      "welsh": "cy",
      "xhosa": "xh",
      "yiddish": "yi",
      "yoruba": "yo",
      "zulu": "zu",
    };

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, "public")));

// Define a route for the homepage
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

app.get("/run", (req, res) => {
  const scriptPath = `"${path.join(__dirname, "../../ASL.py")}"`;
  const lang = req.query.language;
  console.log(langs[lang]);
  exec(`python ${scriptPath} ${lang}`, async (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing x.py: ${error}`);
      res.status(500).send("Internal Server Error");
    } else {
      const lines = stdout.trim().split("\n");
      const lastLine = lines[lines.length - 1];
      console.log(lastLine)
      translatte(lastLine, { from: "en", to: langs[lang] })
        .then((translated) => {
          console.log(translated)
          res.send(translated.text);
        })
        .catch((err) => {
          console.error(err);
        });
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
