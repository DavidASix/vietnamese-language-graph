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

at screen, look to shoulder
So now that we have the what established, lets talk about the how
over the shoulder
Iḿ going to break words down in a tree like format, starting with the end morpheme
Lets say we have 3 morphemes, A B and C. We have a compound word, ABC̣The program will search bvackwards through this word, and connect it to other words in increasing sizẹ, until we get to the full word.
Now I´d say lets get started,
Filp to facing screen with green screen
But Iḿ already done
Show the code
It only took a few loops, but here is our outputted node view. So while this looks good, and basically checks my boxes (show học), there are a lot of dead links and superfluis connection, as well as some missing connections that would improve it further. All of thatś caused by how I coded this together, so Iĺl need to think it over and make some revisions

broll of me walking around and doin things to think it over

shot of me sitting back down and saying
I´ve got iṭ̣ so, Iĺl first process how many morphemes are in each word. Then, for each word, I'll check each smaller word in the data frame to see if its a sub word of my current word. That should give me maximum context for each defined word, and remove all of my dead links. Time to get to work

OTS slow zoom shot timelapse

Alright the code has been revised,


For reference I split out my old code here, then added the new code snippet above and called it from the main function.
You can see I split out the morpheemes, create each possible combination, then check it against the dictionary vales iwth the same length of morphemes
After running my program I've got 23 thousand markdown files which I've imported into Obsidian.