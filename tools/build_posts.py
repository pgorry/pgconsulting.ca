#!/usr/bin/env python3
"""Generate blog/<slug>.html for each case study.

Run from the repo root:  python3 tools/build_posts.py
The output is committed, so GitHub Pages needs no build step.
Posts are listed newest first; "Previous" points to the next older post.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

POSTS = [
    {
        "slug": "relieve-the-pressure",
        "title": "Relieve the pressure",
        "sub": "Augment your own development team",
        "img": "steam.jpg",
        "body": """<p>This client already has a talented development team. But from time to time projects arise that are very difficult to fit into their schedule.<br>&nbsp; &nbsp;</p><p>Working with us allows them to get these time sensitive projects completed on time. In most cases we then help the client transition the projects back in house so that their own development team can learn how they are built and they can do further development and maintenance.<br>&nbsp;<br>Of course we are always on hand should the pressure build again.<br>&nbsp;&nbsp; &nbsp;<br><strong>Technologies: .NET, MVC, HTML, CSS, Javascript, Cordova</strong></p>""",
    },
    {
        "slug": "from-idea-to-revenue",
        "title": "From idea to revenue",
        "sub": "Let us help make your idea a reality",
        "img": "idea.jpg",
        "body": """<ul><li>Founder A had the idea. &nbsp;</li><li>Founder B had technical smarts but no time. &nbsp;</li><li>We became their development partner.</li></ul><p>We helped this start-up go from their one page idea to a revenue generating business in less than a year. Through an iterative development process we build the back end business system, a RESTful API service, and a kick-ass app for the Apple and Android stores.<br>&nbsp; &nbsp;<br>To top it off we helped them get it all up and running in am Azure deployment that can easily scale.<br>&nbsp; &nbsp;<br><strong>Technologies: MVC, .NET, Angular, API Creation, Cordova, SQL, Azure</strong></p>""",
    },
    {
        "slug": "it-s-not-rocket-science-it-s-far-more-complicated",
        "title": "It's not rocket science, it's far more complicated",
        "sub": "Test Driven Development helps",
        "img": "rocket.jpg",
        "body": """<p>We worked with this client to get an online version of a card game up and running . The rules are so complex, replicating them in code was a real challenge. Also keeping them maintained required that we implemented automated unit tests so the rules engine was always stable.<br>&nbsp;&nbsp; &nbsp;<br>We are now in the process of building an app in Xamarin for them.<br>&nbsp;</p><p><strong>Technologies: MVC, .NET, SQL, HTML, CSS, SignalR, Xamarin, TDD</strong></p>""",
    },
    {
        "slug": "holiday-crunch",
        "title": "Holiday Crunch",
        "sub": "Get cover for your teams holidays",
        "img": "christmas.jpg",
        "body": """<p>So it was December 8th and there was a big promotion planned to start on January 2nd. &nbsp;The agency had the creative done for an online game that needed to be in place to support the marketing roll-out.&nbsp;</p><p>Of course with Christmas Holidays looming (including all those parties to fit in) - there was no way that the client could make the changes in time for the launch.<br>&nbsp; &nbsp;</p><p>They turned to us - as we have overseas resources that have different holiday schedules. Everybody went on holidays in confidence and when they returned everything was ready to go.<br>&nbsp; &nbsp;<br>It's a Christmas miracle.<br>&nbsp; &nbsp;<br><strong>Technologies: Responsive HTML &amp; CSS, JQuery</strong></p>""",
    },
    {
        "slug": "we-need-it-yesterday",
        "title": "We need it, yesterday.",
        "sub": "Add extra capacity when deadlines loom.",
        "img": "calendar.jpg",
        "body": """<p>The creative was ready. The launch date was set. The only problem was the website was not built.<br>&nbsp; &nbsp;<br>This project was a great example of the speed and flexibility that we offer. We were able to quickly add two experienced front-end developers to build and launch this responsive website in less than two weeks.<br>&nbsp; &nbsp;<br>We are kind of like cloud computing for software development, ramp us up when needed - don't pay when not needed.<br>&nbsp; &nbsp;<br><strong>Technologies: HTML, CSS, Javascript.</strong></p>""",
    },
    {
        "slug": "processes-and-systems",
        "title": "Processes and Systems",
        "sub": "Putting an end to cowboy coding",
        "img": "gears.jpg",
        "body": """<p>This client had a successful software business with many active clients for a number of years. &nbsp;However as they scaled they found it troublesome, with releases and changes introducing bugs in already functioning code.</p><p>We worked with them to get some release processes in place as well as setting them up with better source control and branching methodologies.</p><p>We also helped move their solution to Azure to help manage their infrastructure costs and make it easier to scale.</p><p>Automated deployment and testing are next on the agenda to make this company a well oiled machine</p>""",
    },
    {
        "slug": "there-must-be-a-better-way",
        "title": "There must be a better way",
        "sub": "Automate those manual jobs",
        "img": "excavators.jpg",
        "body": """<p>This client had a manual process to reconcile their orders once a quarter between two different systems. This involved running an export from one on-line system and then manually entering the orders into Microsoft RMS.<br>&nbsp; &nbsp;<br>We worked with them to build an end to end system. It was scheduled to run nightly and import the days orders from the online order system, convert into the format required by the RMS and then record the entries.<br>&nbsp; &nbsp;<br>This system is designed to run seamlessly without any user intervention - saving not only time but removing a manual process that no one liked doing.<br>&nbsp; &nbsp;<br><strong>Technologies: .NET, MVC, API Integration, SQL</strong></p>""",
    },
    {
        "slug": "that-was-easy",
        "title": "That was easy!",
        "sub": 'We can also do the "simple" stuff',
        "img": "code-bw.jpg",
        "body": """<p>Not all companies or projects require the latest and greatest technologies.</p><p>This client uses us on an ongoing basis to keep their websites up to date and integrate third part services like shopping carts, blogs and social feeds.<br>&nbsp;&nbsp; &nbsp;<br><strong>Technologies: HTML, CSS, Javascript, 3rd party integrations</strong></p>""",
    },
    {
        "slug": "it-s-an-emergency",
        "title": "It's an emergency",
        "sub": "Kind of like calling the plumbers.",
        "img": "batman.jpg",
        "body": """<p>"Okay so we need an update on our Wordpress site - but our developer is long gone. How are we make that change for tomorrow?"<br>&nbsp; &nbsp;<br>The task was simple but this recruitment agency just had no-one available with development skills. The request came in on a Tuesday afternoon and by Wednesday morning we had an experienced Wordpress developer make and test the required changes.<br>&nbsp; &nbsp;<br>All that we were missing was the cape!<br>&nbsp;&nbsp; &nbsp;<br><strong>Technologies: Wordpress &amp; PHP</strong></p>""",
    },
]

ICONS = {
    "Facebook": '<path d="M11 20v-7h2.3l.4-2.7H11V8.6c0-.8.2-1.3 1.3-1.3h1.4V4.9c-.3 0-1.1-.1-2-.1-2 0-3.4 1.2-3.4 3.5v2H6V13h2.3v7z"/>',
    "X": '<path d="M5 5h3.2l3.1 4.3L15 5h1.6l-4.6 5.3L17 15H13.8l-3.3-4.6L6.4 15H4.8l5-5.6z" transform="translate(0 0)"/>',
    "LinkedIn": '<path d="M5 8h2.4v7.5H5zM6.2 4.3a1.4 1.4 0 110 2.8 1.4 1.4 0 010-2.8zM8.9 8h2.3v1c.3-.6 1.1-1.2 2.3-1.2 2.4 0 2.9 1.6 2.9 3.7v4H14v-3.6c0-.9 0-2-1.2-2s-1.5 1-1.5 1.9v3.7H8.9z"/>',
    "Email": '<path d="M4 6h12v.6L10 10.4 4 6.6zm0 2 6 3.8L16 8v6H4z"/>',
}

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="https://www.pgconsulting.ca/assets/img/{img}">
  <meta property="og:url" content="{url}">
  <link rel="canonical" href="{url}">
  <link rel="icon" href="/assets/img/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/site.css">
</head>
<body>
  <a class="back-btn" href="/">&lsaquo;&nbsp; Return to site</a>
  <header class="post-hero" style="background-image:url(/assets/img/{img})">
    <div class="inner">
      <h1 class="title">{title}</h1>
      <p class="sub">{sub}</p>
    </div>
  </header>
  <main class="post">
    <div class="post-body">
{body}
    </div>
    <nav class="post-nav">
{prev}
{next}
    </nav>
    <div class="post-foot">
      <a href="/">&lsaquo;&nbsp; Return to site</a>
      <div class="share">
{share}
      </div>
    </div>
  </main>
</body>
</html>
"""


def text_of(html: str) -> str:
    import re
    t = re.sub(r"<[^>]+>", " ", html).replace("&nbsp;", " ").replace("&amp;", "&")
    return re.sub(r"\s+", " ", t).strip()


def nav_link(post, label, cls):
    if not post:
        return "      <span></span>"
    return (f'      <a class="{cls}" href="/blog/{post["slug"]}"><small>{label}</small>'
            f'<span>{escape(post["title"])}</span></a>')


def share_links(url, title):
    from urllib.parse import quote
    u, t = quote(url, safe=""), quote(title, safe="")
    hrefs = {
        "Facebook": f"https://www.facebook.com/sharer/sharer.php?u={u}",
        "X": f"https://twitter.com/intent/tweet?url={u}&text={t}",
        "LinkedIn": f"https://www.linkedin.com/sharing/share-offsite/?url={u}",
        "Email": f"mailto:?subject={t}&body={u}",
    }
    out = []
    for name, href in hrefs.items():
        target = "" if name == "Email" else ' target="_blank" rel="noopener"'
        out.append(f'        <a href="{escape(href)}" aria-label="Share on {name}"{target}>'
                   f'<svg viewBox="0 0 20 20">{ICONS[name]}</svg></a>')
    return "\n".join(out)


def main():
    out_dir = ROOT / "blog"
    out_dir.mkdir(exist_ok=True)
    for i, p in enumerate(POSTS):
        older = POSTS[i + 1] if i + 1 < len(POSTS) else None
        newer = POSTS[i - 1] if i > 0 else None
        url = f"https://www.pgconsulting.ca/blog/{p['slug']}"
        html = TEMPLATE.format(
            title=escape(p["title"]),
            sub=escape(p["sub"]),
            img=p["img"],
            url=url,
            desc=escape(text_of(p["body"])[:180]),
            body="      " + p["body"],
            prev=nav_link(older, "&lsaquo; Previous", "prev"),
            next=nav_link(newer, "Next &rsaquo;", "next"),
            share=share_links(url, p["title"]),
        )
        (out_dir / f"{p['slug']}.html").write_text(html, encoding="utf-8")
        print("wrote", f"blog/{p['slug']}.html")


if __name__ == "__main__":
    main()
