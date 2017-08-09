Brigit is a project that I began working on at some point in time. You can find the source code on the 
[github page](https://github.com/EriKBZ/brigit). Essentially Brigit is a program that will a compile text into a directed
that can be used to maintain the state of a "story". Basically it lets you play through a choose your own adventure game.
There were some other projects that would do similar things, one project that I looked at was Inkle. There parser and compiler
is leagues better than what I created, but I wanted some different features, like embedding emotional expressions in player
choices to set off sound effects or animations, setting time limits on dialog boxes, or changing background images. Chances
are I could have added these features to Inkle, but I wanted to create something from scratch to get a better since of regex,
grammars, and parsing.  
  
The language went through some revisions as well as the underlying graph. The first iteration was incredibly verbose
and had way too many symbols left and right.

    [res char:person1 background:sunset]
        Speech goes here  
	[*]
	[res char:person2]
		Response to speech goes here
	[*]
	[rep]
		[r] Some choice for player to choose [*]
		[r] Other response [*]
	[*]
  
I based the markup off of XML and HTML with the <open tag> and <close tag> concept. Originally I had begun creating a toy browser
called "Citi browser" by following a tutorial made by a mozilla developer learning Rust. It helped me gain a better understanding
of nuances between different languages, since I was writing Citi browser in C#, not Rust. It so happened that I had just taken a
class on languges and state machines as well which helped practice the knowledge I had just about forgotton 2 days after the
final exam.  
  
Since the tutorial mainly focused on creating an HTML parser and conveting it to a DOM struct, I begun to wonder if how I could
change the project to help the high-school dream of making a game with my friend Alex. It seemed easy enough to parse an HTML like
file into a graph structure that one could traverse. It would help mantain the state of a story. After I tried the first version
above, the whole project somewhat worked but it was very difficult to add features and mantain the code. There was no plan
going in so the code was more of a scrambled mess of spaghetti.  
  
In comes my internship at Gallup, and I had been working Brigit on and off for about 7 months. My first couple of tasks were not
to write any code, but to research first. We were using agile so the first sprint was mostly research, the second was a lot
planning, and then the thrid was actually writing the code out. Taking this into consideration I began rewriting Brigit.
Abstraction was the key, so unlike before where the details of a single speech bubble were stored in it's on data structure
that also acted as a node in a Graph, they were now seperated. Further single speech bubble was no longer it's own structure
and they were stored in a bigger struct. If a single character said something, there would only be one node holding a reference
to it where before if a character said 4 things in a row, then there would be 4 nodes, with repeating information like character
for that speech bubble. Now it is a single node with multiple bubbles contained for a single character. This means that the
the info fetcher will have to act slightly differently.

	CharacterName:
		What the character says*
		Some more things the chracter says*
		The last thing this charcter says**
	
	@player:
		A possible choice*
		Another possible choice*->BranchNameToExecute
		The last choice*->{
			# This is syntax for a branch that executes when this choice
			# is chosen
		}*


