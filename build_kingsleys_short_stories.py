import re
import os

with open("the-great-christmas-disaster-book-page.html", "r", encoding="utf-8") as f:
    template = f.read()

books = [
    {
        "id": "1",
        "title": "A Santa Hat and A Cowboy Song",
        "file": "santa-hat-cowboy-song-book-page.html",
        "cover": "01-KR A Santa Hat and A Cowboy Song.jpg",
        "link": "https://amzn.to/4uDSFc2",
        "blurb": "<h2>One ranch. One fake Santa. One real shot at love.</h2><p>At Saddle Ridge Ranch, Christmas comes with cocoa, hayrides, and one seriously suspicious Santa. Lacey Carmichael has spreadsheets to balance and tinsel to untangle—she does not have time for flirtatious seasonal ranch hands with secrets tucked under their cowboy hats. But when Easton Bishop volunteers to play Santa at the ranch's kids' holiday party—including one very special Kingsley grandkid—Lacey's perfectly wrapped plans start to unravel.</p><p>He's charming. He's talented. And he's definitely hiding something.</p><p class=\"book-meta\">Turns out, the man in red might just be country royalty...and the greatest threat to Lacey's tightly guarded heart.<br>A sweet holiday short full of small-town magic, identity mix-ups, and one unforgettable sleigh bell kiss.</p>"
    },
    {
        "id": "2",
        "title": "Bylines and Boots",
        "file": "bylines-and-boots-book-page.html",
        "cover": "02-KR Bylines and Boots no Xmas.jpg",
        "link": "https://amzn.to/3PJOdIy",
        "blurb": "<h2>A city journalist. A grumpy ranch manager. One unexpected partnership under the Montana sky.</h2><p>When freelance writer Joanna Ray arrives at Saddle Ridge Ranch to cover the launch of their dude ranch season, she's expecting rustic charm, photogenic trails, and a week of lighthearted interviews. What she doesn't expect is being roped into a scavenger hunt with Wyatt McClain—the quiet, no-nonsense ranch manager who'd rather herd cattle than chat with guests.</p><p>Wyatt values order, solitude, and silence. Joanna brings questions, opinions, and a spark he didn't see coming. As they navigate mishaps, trail rides, and campfire assignments together, their unexpected chemistry simmers beneath their bickering. But when Wyatt discovers her notebook and misreads her intentions, the fragile trust between them is put to the test.</p><p class=\"book-meta\">In a town full of second chances and starry skies, can a guarded cowboy and a restless writer find common ground—and maybe even love?<br>A sweet, swoony romance perfect for fans of small-town charm, cowboys with hidden depths, and heroines who aren't afraid to get their boots dirty.</p>"
    },
    {
        "id": "3",
        "title": "Sage and Spurs",
        "file": "sage-and-spurs-book-page.html",
        "cover": "03-KR Sage and Spurs.jpg",
        "link": "https://amzn.to/4lCvf2o",
        "blurb": "<h2>Fresh herbs, frayed nerves, and a slow-burn romance under the Montana sun.</h2><p>Courtney Flannery's restaurant dream is just weeks from opening when her produce supplier backs out, leaving her scrambling for a solution. The only option? Dylan Rivera, the straightforward, quietly dependable foreman of Kingsley's high-yield crop operation. He's got the sage, kale, and basil she needs—along with an unshakable work ethic and a knack for getting under her skin.</p><p class=\"book-meta\">What starts as a business arrangement turns into a season of early-morning harvests, kitchen taste-tests, and more than a few stubborn disagreements. But between the rows of green and the steady rhythm of small-town life, Courtney begins to see the man behind the measured words. And as the days grow longer, so does the quiet pull between them—proving that some of the best things in life, like a perfect harvest, can't be rushed.</p>"
    },
    {
        "id": "4",
        "title": "Boots, Vows, and Second Chances",
        "file": "boots-vows-second-chances-book-page.html",
        "cover": "04-KR Boots, Vows and Second Chances.jpg",
        "link": "https://amzn.to/4sLVRAC",
        "blurb": "<h2>She was supposed to marry her high school sweetheart. Instead, she fell for a cowboy…and his pig.</h2><p>When Kennedy Hall ditched her Napa vineyard wedding, she never imagined she'd end up in Montana, trading heels for muddy boots on her Uncle Colt's sprawling ranch. Cattle, horses, sheep—and yes, a pen full of very opinionated pigs—keep the place running, and her temporary job is to help manage the eco-rental cabins while she figures out her next move.</p><p>Enter Reed Wagner. Brooding, maddeningly capable, and far too easy on the eyes, Reed knows his way around a fence post…and apparently her heart. He's sworn off love, and she's sworn off making herself too needed, but the sparks between them are one chore they can't seem to ignore.</p><p class=\"book-meta\">Between runaway piglets, wedding banquets in a barn, and more cinnamon turnovers than is strictly decent, Kennedy starts to wonder if this ranch life is exactly what she's been missing.</p>"
    },
    {
        "id": "5",
        "title": "Butterflies and Bridles",
        "file": "butterflies-and-bridles-book-page.html",
        "cover": "05-KR Butterflies and Bridles blue sky.jpg",
        "link": "https://amzn.to/4uBB2JF",
        "blurb": "<h2>She came for classroom credit…not a lesson in love.</h2><p>Marina Lopez, a dedicated middle school teacher from Missoula, signs up for a summer program at the Kingsley Ranch to earn in-service hours—and maybe a little perspective. She expects to observe equine therapy with at-risk kids, take notes, and head back to her classroom in the fall. What she doesn't expect is Nate Everhart, the ranch's patient but rugged instructor, whose quiet strength and flashes of humor make every dusty afternoon unforgettable.</p><p>Nate knows the power of horses to heal—and he's seen more than a few volunteers quit once they realize ranch life isn't all wide skies and pretty sunsets. But Marina surprises him with her willingness to try, her kindness with the kids, and the way she lights up the arena just by being there.</p><p class=\"book-meta\">What begins as a professional commitment slowly turns into something neither of them expected: shared laughter, stolen glances, and rides across the Montana hills that feel like freedom. Yet with Marina's world pulling her back to Missoula and Nate's life rooted at the ranch, they'll have to decide if what's growing between them is only a fleeting summer connection—or the start of something worth holding on to.</p>"
    },
    {
        "id": "6",
        "title": "Raindrops and Saddles",
        "file": "raindrops-and-saddles-book-page.html",
        "cover": "06-Raindrops and Saddles.jpg",
        "link": "https://amzn.to/4bk7pVZ",
        "blurb": "<h2>She swore off saddles. He swore off the circuit. But love has other plans.</h2><p>Fletcher Hines swore he was done chasing eight seconds of glory. With a busted shoulder and a future he can't quite face, quiet work at Blue Spur Ranch seems like the perfect hiding place—no arenas, no crowds, just horses…and the ache he won't admit.</p><p>Simone Woodley hasn't touched a saddle since the fall that shattered her riding career and her confidence. But when her vet friend nudges her toward Blue Spur to snap a few photos, she doesn't expect to run into a wrangler who reads horses better than people—and who sees straight through her defenses.</p><p class=\"book-meta\">As Fletch coaxes Simone back to the rail and into the round pen, she forces him to imagine a life beyond the rodeo chute. But when a summer storm hits and one rain-soaked ride changes everything, both are faced with the same choice: cling to the fear that's kept them safe…or risk everything for the chance to heal together.<br>Heartfelt, romantic, and filled with small-town ranch charm, Raindrops and Saddles is a sweet short story about second chances, quiet courage, and love that's worth holding on to.</p>"
    },
    {
        "id": "7",
        "title": "Touchdowns and Tulips",
        "file": "touchdowns-and-tulips-book-page.html",
        "cover": "07-KR Touchdowns and Tulips.jpg",
        "link": "https://amzn.to/478q0BR",
        "blurb": "<h2>Sparks fly on the sidelines when small-town gossip turns one impulsive kiss into something much bigger…</h2><p>April McCarthy never expected to become a guardian to her twelve-year-old nephew. But after her sister's passing, she's determined to give Owen the stability he deserves—even if that means balancing her physical therapy patients with snack duty at Blue Spur Ranch's brand-new flag football program.</p><p>Coach Tate Adler isn't looking for love. Between mentoring his middle school players and dodging questions about why he's still single, romance is the last thing on his playbook. But as their partnership on the sidelines turns into something harder to ignore, the town starts connecting dots that April and Tate aren't ready to draw.</p><p class=\"book-meta\">Now they must navigate meddling neighbors, unexpected chemistry, and feelings that refuse to stay on the sidelines. As Owen finds confidence on the field—and in his new life—April has to decide if guarding her heart is worth missing the biggest win of all.<br>Touchdowns and Tulips is a heartwarming Kingsley short story filled with flirty banter, small-town charm, and a love story that proves sometimes the best plays happen off the field.</p>"
    },
    {
        "id": "8",
        "title": "Coffee Cups and Corrals",
        "file": "coffee-cups-corrals-book-page.html",
        "cover": "08-KR Coffee Cups and Corals.jpg",
        "link": "https://amzn.to/47NAxlZ",
        "blurb": "<h2>He was only passing through. She wasn't.</h2><p>Clay Everitt came to Saddle Ridge Ranch with a plan: lead a corporate team-building retreat, fix what was broken, and head back to his life in Salt Lake City. The ranch was temporary. So was everything else.</p><p>Jessa Hyland knows that real leadership can't be forced, and neither can connection. She's seen plenty of guests come and go, and she doesn't mistake passing moments for promises.</p><p>But between early mornings, shared coffee, stubborn horses, and good conversations, something unexpected began to take shape. Clay started to question what he's been missing, and Jessa discovered that even temporary people can leave lasting impressions.</p><p class=\"book-meta\">They both know how this ends. He'll leave. She'll stay. So why does walking away feel so hard?<br>Coffee Cups and Corrals is a clean, heartwarming romance about unexpected insight and the kind of connection that lingers long after it's over.</p>"
    }
]

for b in books:
    html = template
    html = html.replace("The Great Christmas Disaster Book Page", b["title"] + " Book Page")
    html = html.replace("Love Only #1", f"The Kingsleys Short Story #{b['id']}")
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
        
print("Successfully generated Kingsleys short story book pages.")
