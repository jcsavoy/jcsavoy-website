import re
import os

with open("the-great-christmas-disaster-book-page.html", "r", encoding="utf-8") as f:
    template = f.read()

books = [
    {
        "id": "2",
        "title": "Tidal Rivals",
        "file": "tidal-rivals-book-page.html",
        "cover": "02-LO TIDAL RIVALS.jpg",
        "blurb": "<h2>She came to fix the harbor. He'd spent fifteen years making sure it didn't need fixing.</h2><p>Tourism consultant Peyton Tremont arrives in Cliffhaven, Maine, with a sixty-slide PowerPoint and a plan to transform the waterfront. Marina owner Grant Carpenter has a plan too. It’s scribbled on a napkin in three sentences.</p><p>When they discover they're bidding on the same historic building—her for a flashy tourist center, him to protect the local boatyard—the competition is on. But somewhere between her nine hundred photographs and his three-word solutions, rivalry starts looking a lot like partnership.</p><p>With a meddling scone baker, a lobsterman who speaks in weather reports, and a barista whose silence says everything, the town of Cliffhaven has loud opinions about these two. Now Peyton has to choose: the career she spent twelve years building, or the harbor that rebuilt her.</p><p class=\"book-meta\">Tidal Rivals is a sweet romantic comedy about two stubborn people, one small town, and the building that argued them into love.</p>"
    },
    {
        "id": "3",
        "title": "High Tide High Jinks",
        "file": "high-tide-highjinks-book-page.html",
        "cover": "3-LO HIGH TIDE HIGIJINKS.jpeg",
        "blurb": "<h2>She talks to sea creatures. He writes incident reports. Cliffhaven thinks they're perfect for each other.</h2><p>Marine biologist Sharon Powell came to Cliffhaven, Maine, to study sea creatures. She did not come to be rescued from a tide pool by the most annoyingly calm Coast Guard officer on the Atlantic seaboard.</p><p>But when the town requires her to coordinate fieldwork with Lieutenant Zach Miller's patrol schedule, her six-month research grant becomes a daily negotiation between a woman who treats \"calculated risk\" as a job description and a man who rations his smiles like emergency supplies.</p><p>Then Zach copies two hundred and sixteen pages of handwritten tidal records because he thinks she'll find them useful. He adjusts his patrol route by twelve minutes. And when a government agency threatens to destroy her research site, the man assigned to facilitate? Also Zach.</p><p class=\"book-meta\">In a town where the bakery owner dispenses wisdom with scones and the florist considers everyone's love life a personal project, Sharon has to decide what scares her more: losing her research or admitting she doesn't want to leave.</p>"
    },
    {
        "id": "4",
        "title": "The Wedding Fakers",
        "file": "the-wedding-fakers-book-page.html",
        "cover": "4-LO THE WEDDING FAKERS.jpg",
        "blurb": "<h2>Penny Crawford is excellent at planning other people’s happily-ever-afters. Her own love life? Still buffering.</h2><p>When a browser autofill error RSVPs her to Cliffhaven’s Valentine’s fundraiser with a plus-one she doesn’t have, Penny does what any reasonable person would do: she panics and describes her imaginary dream date to a shelf of folded tablecloths in a storage closet.</p><p>Unfortunately, the exact firefighter she just described is standing behind her.</p><p>Derek Wilson has been someone’s convenient date before—and it never ends well. So when the town’s new wedding planner needs a fake boyfriend for one night, every instinct tells him to walk away. But after Penny reorganizes his firehouse kitchen in under ten minutes, debates canned goods with surprising intensity, and leaves what can only be described as a yogurt eulogy in his fridge, walking away becomes… complicated.</p><p>One fake date turns into four. Then Derek’s sister hires Penny to plan her wedding. Brides start calling to ask for that cute firefighter to help, and somehow, Penny’s calendar fills up with clients who are absolutely convinced she and Derek are Cliffhaven’s newest love story.</p><p>The town thinks they’re a couple, and the lie is multiplying faster than Penny can color-code it. And the feelings? Those stopped being fake a long time ago.</p><p class=\"book-meta\">A clean, sweet rom-com set in charming Cliffhaven, Maine—where gossip travels at the speed of baked goods, and the local chef has been waiting three years to serve a soufflé for two.</p>"
    },
    {
        "id": "5",
        "title": "The Lighthouse Invasion",
        "file": "the-lighthouse-invasion-book-page.html",
        "cover": "05-LO THE LIGHTHOUSE INVASION.jpg",
        "blurb": "<h2>She invaded his silence. He built her a reason to stay.</h2><p>Jamie Crenshaw's dressmaking shop gets shut down by a gas leak in the middle of sewing seventeen costumes for Cliffhaven's Heritage Festival. Harriet Ogle has a solution: move everything into the historic lighthouse cottage. Harriet does not mention that the cottage already has a very reluctant resident.</p><p>Trevor Morrison likes his life orderly, quiet, and free of women who talk to dress forms, sing the wrong lyrics to every song, and leave pins in his butter dish.</p><p>Jamie only needs the space for six weeks. Trevor only needs his sanity to survive it. But somewhere between midnight sewing sessions and lighthouse logs that start including entries like \"Dressmaker arrived 6:15. Singing commenced 6:19. Lyrics: nonstandard\" — neither of them plans for the biggest disruption of all.</p><p class=\"book-meta\">She stops packing. He starts building furniture nobody asked for. And the temporary arrangement stops being temporary.</p>"
    },
    {
        "id": "6",
        "title": "The Float Fiasco",
        "file": "the-float-fiasco-book-page.html",
        "cover": "6-LO COASTAL CAROLS.jpg",
        "blurb": "<h2>Three hundred and fifty pinwheels. One clipboard. Zero professional detachment.</h2><p>Kaylee Andrews came back to Cliffhaven to help her mother. She stayed to open a design studio. She did not stay to build a parade float so ambitious it might require Coast Guard intervention.</p><p>Lucas Ryan is the Coast Guard intervention.</p><p>Three things Kaylee knows for certain:<br>• The float needs to be spectacular.<br>• \"Just one small improvement\" has never once meant what she thinks it means.<br>• She is absolutely, definitely not developing feelings for the safety coordinator who keeps showing up with coffee and correct opinions about bolt placement.</p><p>Lucas knows one thing: his patrol route has been drifting toward Harbor Street for six months, and the clipboard stopped being the reason approximately three weeks ago.</p><p class=\"book-meta\">In a small Maine harbor town where the baker delivers opinions with scones, the harbormaster predicts weather with his elbow, and no one has boundaries, a parade float is never just a parade float. Especially when the designer and the safety coordinator stop pretending the clipboard is the reason he keeps showing up.</p>"
    }
]

for b in books:
    html = template
    html = html.replace("The Great Christmas Disaster Book Page", b["title"] + " Book Page")
    html = html.replace("The Great Christmas Disaster", b["title"])
    html = html.replace("Love Only #1", "Love Only #" + b["id"])
    html = html.replace("1-LO The Great Christmas Disaster.jpg", b["cover"])
    html = html.replace("the-great-christmas-disaster-book-page.html", b["file"])
    
    # Replace Button
    html = html.replace("<a href=\"https://amzn.to/476J978\" target=\"_blank\" class=\"btn btn-primary\" rel=\"noopener\">Buy on Amazon </a>", 
                        "<button class=\"btn btn-primary\" style=\"cursor:not-allowed; opacity:0.7;\" disabled>COMING SOON</button>")
    
    # Replace blurb
    html = re.sub(r"<div id=\"blurb\" class=\"book-blurb\">.*?</div></div></section>", 
                  "<div id=\"blurb\" class=\"book-blurb\">" + b["blurb"] + "</div></div></section>", html, flags=re.DOTALL)
                  
    with open(b["file"], "w", encoding="utf-8") as f:
        f.write(html)
        
print("Successfully generated 5 book pages.")
