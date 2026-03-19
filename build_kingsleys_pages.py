import re
import os

with open("the-great-christmas-disaster-book-page.html", "r", encoding="utf-8") as f:
    template = f.read()

books = [
    {
        "id": "1",
        "title": "Santa Cowboy",
        "file": "santa-cowboy-book-page.html",
        "cover": "1-KR Santa Cowboy.jpg",
        "link": "https://amzn.to/47NBHhl",
        "blurb": "<h2>One party planner, one grumpy cowboy, and one tiny letter to Santa Cowboy… what could possibly go wrong (or wonderfully right)?</h2><p>Hallie Whitmore is a Dallas-based party planner with zero interest in sleigh bells, sentiment, or staying put. But when she inherits her grandmother’s old Victorian farmhouse in Cottonwood Ridge, Montana, a quick flip-and-sell turns complicated—especially when a letter addressed to Santa Cowboy ends up in her mailbox.</p><p>Beau Kingsley—grumpy cowboy, former rodeo star, and not-so-retired Santa Cowboy—has no intention of stepping back into those boots. But a local kid still believes, and the town hasn’t forgotten the Christmas magic once made in that big white farmhouse.</p><p>The Kingsley family practically owns Cottonwood Ridge—and they’re all-in on bringing back the beloved holiday celebration. Between Ridge’s over-the-top Dude Ranch gala and Colt’s hayrides featuring pigs in Santa hats, the whole town is going full on Christmas.</p><p>Somewhere between tangled lights and cocoa stations, Hallie winds up at the center of a celebration she never planned… and next to the one cowboy who just might change everything.</p><p class=\"book-meta\">A cozy, billionaire cowboy sweet romance filled with slow-burn charm, small-town warmth, found family, and holiday magic in every snowflake.</p>"
    },
    {
        "id": "2",
        "title": "Saddle Up, Cowgirl",
        "file": "saddle-up-cowgirl-book-page.html",
        "cover": "2-KR Saddle Up, Cowgirl.jpg",
        "link": "https://amzn.to/4dtyEhZ",
        "blurb": "<h2>She doesn’t do cowboys. He doesn’t do second chances.</h2><p>Sawyer Kingsley isn’t looking for love—he’s too busy running the family ranch and raising his eight-year-old son to entertain the idea of dating. After losing his wife, he built walls higher than the hayloft and settled into a life of quiet routine. Until a horse emergency brings a new vet to his barn—and something shifts.</p><p>Dr. Willa Hart came to Cottonwood Ridge for a fresh start, not a flirtation with the local cowboy widower. Smart, capable, and completely uninterested in getting involved, she tells herself it’s just a farm call. Just a horse. Just a kid. Just a man with eyes too kind for her comfort.</p><p>But as Willa becomes entangled in Kingsley family antics and small-town charm, the lines she’s drawn around her heart start to blur. Especially when her past comes calling—and Sawyer’s hit with a custody battle that changes everything.</p><p class=\"book-meta\">A tender, slow-burn romance about second chances, found family, and opening the gate again—even when you’re not sure what’s waiting on the other side.</p>"
    },
    {
        "id": "3",
        "title": "Rescue Me, Cowboy",
        "file": "rescue-me-cowboy-book-page.html",
        "cover": "3-KR Rescue Me, Cowboy.jpg",
        "link": "https://amzn.to/4uCE3tf",
        "blurb": "<h2>He came for the quiet. She offered connection. Love wasn't part of the plan… but it might just be the rescue they both need.</h2><p>When Callum Kingsley trades his snow-covered cattle ranch in Saskatchewan for a work breather in sunny Cottonwood Ridge, he expects solitude—not stampeding goats and a surprise yoga class. Burned out and skeptical of all things woo-woo, Callum just wants to evaluate a parcel of Kingsley land for an eco-grazing program and head back north.</p><p>Enter Ren Holloway—serenity in motion with a stubborn herd of goats and a knack for turning chaos into calm. With her goat yoga retreats, handmade soaps, and lavender-scented optimism, she’s everything Callum doesn’t understand… and everything he can’t stop thinking about.</p><p>One fencing mishap, a runaway goat, and a forced partnership later, Ren and Callum are co-hosting a wellness weekend neither of them wanted. But as tension turns to teamwork, and friendship starts to flirt with something more, Callum begins to wonder if this peaceful little corner of Montana—and the woman who thrives in it—might just be worth sticking around for.</p>"
    },
    {
        "id": "4",
        "title": "Comeback Cowgirl",
        "file": "comeback-cowgirl-book-page.html",
        "cover": "4-KR Comeback Cowgirl.jpg",
        "link": "https://amzn.to/4lybusQ",
        "blurb": "<h2>Sometimes the road back to yourself runs straight through a cowboy’s heart.</h2><p>When crisis management consultant Kelly Albright loses her biggest client—and her confidence—she never expects her next opportunity to come from Montana. But at her former mentor’s urging, Kelly agrees to spend a month at Kingsley Ranch, helping a legendary rodeo family polish their image before the summer circuit begins.</p><p>What she didn’t see coming was running right into Beckett Kingsley—the rugged, quietly stubborn cowboy who once kissed her as if it were forever… then disappeared without a word.</p><p>With thirty days to prove herself, Kelly must navigate skeptical ranch hands, high-stakes PR, and the man she swore she’d never forgive. But under the wide Montana sky, old sparks don’t stay buried for long.</p><p class=\"book-meta\">A sweet romance about second chances, small-town hearts, and finding the courage to bet everything on love.</p>"
    },
    {
        "id": "5",
        "title": "Christmas Carol Cowgirl",
        "file": "christmas-carol-cowgirl-book-page.html",
        "cover": "5-KR CHRISTMAS CAROL COWGIRL.jpg",
        "link": "https://amzn.to/4792wfS",
        "blurb": "<h2>Sometimes the best gifts aren’t wrapped. They’re found where you least expect them.</h2><p>Four months ago, Faith Kingsley came home to Cottonwood Ridge from Nashville to lick her wounds from the heartbreak she left behind.</p><p>Nashville feels like a world away as she helps out at her sister’s feed store, stacking feed bags and trying to figure out what’s next. She’s sworn off the stage and the spotlight until an unexpected job at the town’s music shop puts a guitar back in her hands and a guarded shop owner in her path.</p><p>Luke Hendricks is determined to keep his grandfather’s store running while the old man recovers, and he isn’t looking for help, especially not from a woman who clearly doesn’t plan to stay. But as the holidays draw near and their lives begin to intertwine, Faith begins to rediscover herself… and what it truly means to come home.</p><p class=\"book-meta\">Set against twinkling lights, cozy family dinners, and a barn full of Christmas carols, Christmas Carol Cowgirl is a sweet, slowburn romance about second chances, unexpected love, and finding your way back to yourself.</p>"
    },
    {
        "id": "6",
        "title": "Trust Me, Cowboy",
        "file": "trust-me-cowboy-book-page.html",
        "cover": "6-KR Trust Me, Cowboy.jpg",
        "link": "https://amzn.to/40FIbLr",
        "blurb": "<h2>One ultimatum. One old friend. Six weeks to discover what love was meant to be.</h2><p>Back in high school, her grandmother warned her about the clause in her Will: marry by thirty or she won't inherit the family law practice. Raven had laughed it off, confident she’d find “real love” someday, though her best friend Zane Kingsley jokingly offered to marry her if she didn’t. At the time, she brushed it aside.</p><p>Now she’s twenty-nine, single, and six weeks from losing everything. Returning to Cottonwood Ridge, Raven hopes to reconnect with Zane, the once shy mechanic who stole her heart. But the man she finds isn’t the boy she remembers. Zane’s confident now, saving every penny to buy his own ranch and build a life on his terms.</p><p>With a rival attorney threatening Raven’s inheritance and another buyer eyeing Zane’s dream property, they both have something to lose and everything to gain if they can trust what’s always been between them.</p><p class=\"book-meta\">Can a promise made in their teens become a love built to last?</p>"
    },
    {
        "id": "7",
        "title": "Walk With Me, Cowboy",
        "file": "walk-with-me-cowboy-book-page.html",
        "cover": "7-KR WALK WITH ME, COWBOY.jpg",
        "link": "https://amzn.to/4sXpuPB",
        "blurb": "<h2>Some journeys take more than one set of reins.</h2><p>Cattle operations manager, Hunter Caldwell, has never shied away from hard work or big responsibility. What he’s never learned is how to make life-changing decisions with someone else.</p><p>When a dream cattle-ranching opportunity puts his future on the line, Hunter makes a choice he believes is right, only to fracture the trust he’s built with Lainey Kingsley, the ranch owner’s daughter.</p><p>Lainey doesn’t doubt his work ethic or his ambition. What she won’t accept is being informed after the fact, as if her place in his life is secondary to his plans.</p><p>With trust on shaky ground and a second chance hovering just out of reach, both Hunter and Lainey must decide what partnership really means—and whether love can grow when the path forward can’t be chosen alone.</p><p class=\"book-meta\">A heartfelt cowboy romance about trust, growth, and choosing a future—together.</p>"
    }
]

for b in books:
    html = template
    html = html.replace("The Great Christmas Disaster Book Page", b["title"] + " Book Page")
    html = html.replace("The Great Christmas Disaster", b["title"])
    html = html.replace("Love Only #1", "The Kingsleys #" + b["id"])
    html = html.replace("1-LO The Great Christmas Disaster.jpg", b["cover"])
    html = html.replace("the-great-christmas-disaster-book-page.html", b["file"])
    
    # Replace Button
    html = html.replace("<a href=\"https://amzn.to/476J978\" target=\"_blank\" class=\"btn btn-primary\" rel=\"noopener\">Buy on Amazon </a>", 
                        f"<a href=\"{b['link']}\" target=\"_blank\" class=\"btn btn-primary\" rel=\"noopener\">Buy on Amazon </a>")
    
    # Replace blurb
    html = re.sub(r"<div id=\"blurb\" class=\"book-blurb\">.*?</div></div></section>", 
                  "<div id=\"blurb\" class=\"book-blurb\">" + b["blurb"] + "</div></div></section>", html, flags=re.DOTALL)
                  
    with open(b["file"], "w", encoding="utf-8") as f:
        f.write(html)
        
print("Successfully generated 7 Kingsleys book pages.")
