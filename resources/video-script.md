# Vietnamese Language Graph

Xin chào, tôi tên là David và tôi đang học Tiếng Việt!

Vietnamese is a really interesting language, and it differes from english in many ways, but the most stark difference I've had to get my head around so far is the low morpheme per word ratio. A morpheme is the smallest meaningful part of a language. So in english, we have words like Running, which contains two morphemes, Run and Ing. We can combine these two get a single word, running.
In Vietnamese, instead of combining the morphemes into a single word, two morphemes which are both full words are chained to make a compound word; đang chạy. đang, meaning currently, and chạy, meaning run.
Vietnamese being an isolating language means that most complicated words or concepts are communicated through these chained compound words. In my learning journey I've come across many words with common root words; For instance the word học means to learn. Học phì means tuition, and học sinh means pupil. So I got to wondering, what other words were based from the word học, and what base words might use học to modify their own meaning?
Well to answer this question I'm building what I've dubbed the Vietnamese language graph. My goal is to make a node based visual representation of these compound words so that I can expand my vocabulary through looking at the branches of the root words.

Breakdown project
I see this project essentially as breaking down into three main steps

- Sourcing the word data
- Parsing the words into a usable format
- Connecting related words
- Displaying these connections in a node graph

Finding the data didn't take long, I figured I would borrow a viet to english dictionary being used in some open source project. I searched google with a github site dork and came across a english to viet dictionary from a Ho Chi Minh univeristy student, cảm ơn Quang Hiển.

Before parsing the data I need to decide how I'm going to display it. I've recently learned of obsidian
We'll create a bunch of markdown files as alll I need is a proof of concept
I will create a sqllite version too though so I can bring this project further If I want in future