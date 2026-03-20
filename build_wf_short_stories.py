import re
import os

with open("the-great-christmas-disaster-book-page.html", "r", encoding="utf-8") as f:
    template = f.read()

books = [
    {
        "id": "1",
        "tag": "Whispering Falls Short Story #1",
        "title": "Love On The Line",
        "file": "love-on-the-line-book-page.html",
        "cover": "01-LOVE ON THE LINE.jpg",
        "link": "https://amzn.to/3NMibes",
        "blurb": "<h2>One phone call, one charming voice, and a customer service mix-up that rewrites everything.</h2><p>When small-town bookstore owner Claire Delaney calls customer service to track down a missing book, the last thing she expects is to enjoy the conversation. But Will, the charming voice on the other end of the line, turns a frustrating mix-up into a playful exchange of literary debates and unexpected chemistry.</p><p>What starts as a series of texts and book challenges takes a surprising turn when Will shows up in Whispering Falls for the weekend. As Claire gives him a tour of her town, their connection deepens, leaving them both wondering—could this be more than just a fleeting chapter?</p><p class=\"book-meta\">A heartwarming short romance about books, banter, and the magic of an unexpected connection.</p>"
    },
    {
        "id": "2",
        "tag": "Whispering Falls Short Story #2",
        "title": "Radio Romance",
        "file": "radio-romance-book-page.html",
        "cover": "02-Radio Romance.jpg",
        "link": "https://amzn.to/40B26ey",
        "blurb": "<h2>Late-night radio brought them together; a snowstorm might just seal the deal.</h2><p>When Whispering Falls radio host Ainsley Jefferson picks up a call from a man who only calls himself Boston Guy, she doesn't expect it to become the best part of her night. But as their witty, intimate conversations grow more personal, she realizes the voice on the line is becoming something she looks forward to more than she should.</p><p>Then a snowstorm knocks out the studio, and Boston Guy appears in person—soft-spoken, steady, and nothing like she expected. Suddenly, their connection is real.</p><p class=\"book-meta\">Set in a snow-draped New England town filled with warmth, wit, and late-night honesty, Radio Romance is a sweet, slow-burn romance about finding comfort in conversation and falling for someone who hears you—even when you're not saying everything out loud.</p>"
    },
    {
        "id": "3",
        "tag": "Whispering Falls Short Story #3",
        "title": "Love, Postmarked, and Delivered",
        "file": "love-postmarked-book-page.html",
        "cover": "03-LOVE, POSTMARKED AND DELIVERED.png",
        "link": "https://amzn.to/475iLdR",
        "blurb": "<h2>She's great with letters—but never expected one to deliver love.</h2><p>Lucy Hart runs Whispering Falls' post office, where the mail's as predictable as the town's gossip—until a vintage postcard lands on her counter with a flirty riddle: <i>Your smile's worth more than a first-class stamp.</i></p><p>Enter Ben Carver, a camera-wielding newcomer with a knack for mystery and a grin that stamps itself on Lucy's heart. As cryptic cards pile up, Lucy's chasing clues through cafés and parks, dodging meddling locals and her own stubborn streak.</p><p class=\"book-meta\">Is Ben's lens focused on her—or just a small-town story? One thing's clear: this romance is postmarked for keeps.</p>"
    },
    {
        "id": "4",
        "tag": "Whispering Falls Short Story #4",
        "title": "Hard Hat, Soft Heart",
        "file": "hard-hat-soft-heart-book-page.html",
        "cover": "04-HARD HAT, SOFT HARD AS ONE.jpg",
        "link": "https://amzn.to/4bjZQ1w",
        "blurb": "<h2>She's got the plans, he's got the tools—together, they're rebuilding more than a lighthouse.</h2><p>Natalie Olsen, museum director with a clipboard and a cause, is dead-set on reviving the Whispering Falls Lighthouse—until Cody Lynch, a brooding ironworker with calloused hands and zero chill, struts in to fix more than just railings. She's got history on her side; he's got a hammer and a knack for ignoring her notes.</p><p class=\"book-meta\">When a storm strands them in the tower, sparks fly hotter than the firelight, trading sass for secrets. From zip-tie battles to a kiss that rewrites the blueprint, these two prove restoring a lighthouse—and a heart—takes grit, guts, and a little mischief.</p>"
    },
    {
        "id": "5",
        "tag": "Whispering Falls Short Story #5",
        "title": "Brewing Up Trouble",
        "file": "brewing-up-trouble-book-page.html",
        "cover": "05-BREWING UP TROUBLE AS ONE.jpeg",
        "link": "https://amzn.to/4lCWkT7",
        "blurb": "<h2>One grumpy barista. One charming writer. One foam heart away from falling for each other.</h2><p>Nora Tate likes her life like she likes her coffee—strong, structured, and absolutely spill-free. But when Jake Ellis, a wandering freelance writer with a grin as messy as his note-filled backpack, strolls into her café and distracts her mid-pour, the result is a ruined latte, a stained shirt, and a challenge she never saw coming.</p><p>What starts as a harmless bet—one lesson in espresso for one lesson in letting go—quickly turns into a flurry of frosting disasters, late-night stargazing, and surprise raccoons (in latte form, of course). Jake isn't supposed to stick around. Nora isn't supposed to care. And yet, the more time they spend together, the harder it is to deny that something's brewing… and it's not just the coffee.</p><p class=\"book-meta\">Filled with sweet steam, small-town sass, and the kind of slow-burn romance that sneaks up when you least expect it, Brewing Up Trouble is a cozy, caffeine-fueled love story with heart—and just a hint of cinnamon.</p>"
    },
    {
        "id": "6",
        "tag": "Whispering Falls Short Story #6",
        "title": "Mat Talk and Mistletoe",
        "file": "mat-talk-mistletoe-book-page.html",
        "cover": "06-Mat Talk and Mistletoe.jpg",
        "link": "https://amzn.to/3P9Gl35",
        "blurb": "<h2>When words falter, love finds a way to pin the heart.</h2><p>Speech therapist Valerie Blanchard came to Whispering Falls to find her footing again, not to fall for the town's grumpiest wrestling coach, who'd rather wrestle a blizzard than warm up to her therapy talk. But when a snowstorm traps her in a gym overnight with Thane Upshaw, her steady calm and his quiet strength collide in unexpected ways.</p><p>Between vending machine dinners, heartfelt confessions, and a flurry of winter moments, Valerie starts to see past Thane's bark. As small-town Christmas magic swirls and a teen wrestler finds his voice with Valerie's help, the walls around Thane's heart begin to crack.</p><p class=\"book-meta\">But with past regrets and stubborn pride between them, will these two opposites find a way to meet under the mistletoe—or let their chance at something real melt away with the snow?<br>A cozy, slow-burn holiday romance full of warmth, wit, and a love that proves steady can still sweep you off your feet.</p>"
    },
    {
        "id": "7",
        "tag": "Whispering Falls Short Story #7",
        "title": "Holly Jolly Mix-Up",
        "file": "holly-jolly-mix-up-book-page.html",
        "cover": "07-HOLLY JOLLY MIX-UP.jpg",
        "link": "https://amzn.to/3NNpFhg",
        "blurb": "<h2>A flirty text. A wrong number. A holiday mix-up that might just be the best thing to ever land in Holly Carter's inbox.</h2><p>With ten days left before winter break, high school English teacher Holly Carter is hanging on by a thread—and a thermos of peppermint cocoa. But when a message meant for her best friend accidentally lands in a stranger's hands, Holly finds herself swept into late-night chats with a mystery man who quotes books and makes her laugh harder than she has in months.</p><p>Nick Armstrong didn't plan to stay long in Whispering Falls. He's just here to help his aunt fix up her cottage before the holidays. But an unexpected text from “some overly festive person named Holly” quickly becomes the highlight of his day. Between trivia nights, tangled garlands, and one snow-drenched dance floor, he begins to suspect the charming teacher he keeps bumping into might be the same Holly lighting up his phone.</p><p class=\"book-meta\">As snow falls and secrets unravel, Holly must decide if she's ready to turn the page—and find out if her texting crush and the real-life guy stealing her heart... are one and the same.</p>"
    },
    {
        "id": "8",
        "tag": "Whispering Falls Short Story #8",
        "title": "Second Chances Under Construction",
        "file": "second-chances-construction-book-page.html",
        "cover": "08-SECOND CHANCES UNDER CONSTRUCTION.jpg",
        "link": "https://amzn.to/3Pl2rj2",
        "blurb": "<h2>She had a crush. He had a secret. Now they've got a second shot—and maybe more than just a shoulder to fix.</h2><p>Physical therapist Marcie Bell swore her return to Whispering Falls was strictly temporary. Patch a few shoulders, dodge small-town gossip, and definitely avoid falling for her high school crush all over again—especially since he's also her best friend's older brother.</p><p>Trevor Devlin is good with his hands—just not so great at talking about feelings. But when Marcie shows up at the clinic, older, bolder, and somehow even more unforgettable, the crush he buried years ago comes back swinging.</p><p class=\"book-meta\">They're co-hosting a booth for the Spring Into Bloom Fair, but the sparks flying between them have nothing to do with wellness. With old feelings resurfacing and new risks on the line, Marcie and Trevor have to decide: is this just a nostalgic detour—or the second chance neither of them saw coming?</p>"
    },
    {
        "id": "9",
        "tag": "Whispering Falls Short Story #9",
        "title": "Dancing In The Moonlight",
        "file": "dancing-moonlight-book-page.html",
        "cover": "09-Dancing In The Moonlight.jpg",
        "link": "https://amzn.to/4sXC3dG",
        "blurb": "<h2>One left foot, one guarded heart… and one unforgettable dance.</h2><p>Ballroom dance instructor Annelise Holder was expecting a seasoned student—not the town's charming, toolbelt-wearing maintenance supervisor. But when Ethan Callahan shows up for lessons to surprise his sister at her wedding, missteps turn into laughter, and reluctant partnership starts to feel like something more.</p><p class=\"book-meta\">With the studio's future on the line, Annelise has no time for distractions. But under the glow of fairy lights and unexpected waltzes, her carefully choreographed life might be ready for a new rhythm… one that includes love.</p>"
    },
    {
        "id": "10",
        "tag": "Whispering Falls Short Story #10",
        "title": "A Listing For Love",
        "file": "listing-for-love-book-page.html",
        "cover": "010-A LISTING OR LOVE.jpg",
        "link": "https://amzn.to/47VlpDc",
        "blurb": "<h2>Twelve houses. Twelve days. One unexpected romance wrapped up in twinkle lights and second chances.</h2><p>When small-town real estate agent Maya Brinkman agrees to help her retiring boss co-list a dozen festive homes before Christmas, she's ready for a holly-jolly sprint to the finish. What she's not ready for is Lucas Vaughn—big-city polished, allergic to tinsel, and the son who's supposed to be helping... or taking over.</p><p>Lucas has one goal: get in, sell fast, and get back to the real world. But as Whispering Falls works its cozy magic, and as Maya's stubborn spark thaws his frozen plans, Lucas finds himself wondering if success might look different than he ever imagined.</p><p class=\"book-meta\">Between snow-dusted porches, sleigh rides, and more than a few holiday mishaps, Maya and Lucas discover that the best homes aren't just built—they're found, together.<br>In Whispering Falls, love might just be the ultimate closing deal.</p>"
    },
    {
        "id": "11",
        "tag": "Whispering Falls Short Stories",
        "title": "Whispering Falls Short Story Collection 1-5",
        "file": "wf-short-stories-1-5-book-page.html",
        "cover": "Stories 1-5.jpg",
        "link": "https://amzn.to/4cWt6MR",
        "blurb": "<h2>Fall head over heels with five sweet, small-town romances—all set in the cozy, quirky charm of Whispering Falls.</h2><p>From unexpected calls to snowy nights and foam hearts, these bite-sized love stories are perfect for a quick escape full of heart and happily-ever-afters.</p><p class=\"book-meta\">Cozy up with these feel-good, fast-read romances where the sparks are sweet, the kisses are meaningful, and love always finds its way—one short story at a time.</p>"
    },
    {
        "id": "12",
        "tag": "Whispering Falls Short Stories",
        "title": "Whispering Falls Short Story Collection 6-10",
        "file": "wf-short-stories-6-10-book-page.html",
        "cover": "stories 6-10.jpg",
        "link": "https://amzn.to/4sk5LJJ",
        "blurb": "<h2>Five more heartwarming short stories from Whispering Falls—where love shows up in the most unexpected ways, especially around the holidays.</h2><p>These sweet, feel-good romances are perfect for cozy nights, festive lights, and happily-ever-afters wrapped in charm.</p><p class=\"book-meta\">Come home to Whispering Falls with these short and sweet love stories that are brimming with charm, laughter, and just the right dose of holiday magic.</p>"
    }
]

for b in books:
    html = template
    html = html.replace("The Great Christmas Disaster Book Page", b["title"] + " Book Page")
    html = html.replace("Love Only #1", b["tag"])
    html = html.replace("1-LO The Great Christmas Disaster.jpg", b["cover"])
    html = html.replace("The Great Christmas Disaster", b["title"])
    html = html.replace("the-great-christmas-disaster-book-page.html", b["file"])
    
    # Replace Button
    if b["link"]:
        btn_replacement = f"<a href=\"{b['link']}\" target=\"_blank\" class=\"btn btn-primary\" rel=\"noopener\">Buy on Amazon </a>"
    else:
        btn_replacement = "<button class=\"btn btn-primary\" style=\"cursor:not-allowed; opacity:0.7;\" disabled>COMING SOON</button>"
        
    html = html.replace("<a href=\"https://amzn.to/476J978\" target=\"_blank\" class=\"btn btn-primary\" rel=\"noopener\">Buy on Amazon </a>", btn_replacement)
    
    # Replace blurb
    html = re.sub(r"<div id=\"blurb\" class=\"book-blurb\">.*?</div></div></section>", 
                  "<div id=\"blurb\" class=\"book-blurb\">" + b["blurb"] + "</div></div></section>", html, flags=re.DOTALL)
                  
    with open(b["file"], "w", encoding="utf-8") as f:
        f.write(html)
        
print("Successfully generated Whispering Falls short story book pages.")
