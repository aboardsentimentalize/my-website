#!/usr/bin/env python
"""Update press.html to match reference site layout"""

HTML_CONTENT = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Press - Stephanie Shum</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #222;
            background-color: #fff;
        }

        header {
            text-align: center;
            padding: 60px 20px 40px;
            border-bottom: 1px solid #e5e5e5;
        }

        h1 {
            font-size: 3em;
            font-weight: 300;
            margin-bottom: 10px;
            letter-spacing: 2px;
        }

        .tagline {
            font-size: 1.2em;
            color: #666;
            font-weight: 300;
        }

        nav {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 30px;
            padding: 30px 20px;
            background-color: #fafafa;
        }

        nav a {
            text-decoration: none;
            color: #333;
            font-size: 0.95em;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 500;
            transition: color 0.3s;
        }

        nav a:hover {
            color: #999;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 60px 20px;
        }

        .page-title {
            font-size: 2.5em;
            font-weight: 300;
            text-align: center;
            margin-bottom: 60px;
        }

        .press-item {
            display: flex;
            gap: 30px;
            margin-bottom: 50px;
            padding-bottom: 50px;
            border-bottom: 1px solid #e5e5e5;
        }

        .press-item:last-child {
            border-bottom: none;
        }

        .press-image {
            flex-shrink: 0;
            width: 250px;
        }

        .press-image img {
            width: 100%;
            height: auto;
            display: block;
        }

        .press-content {
            flex: 1;
        }

        .press-item h3 {
            font-size: 1.8em;
            font-weight: 400;
            margin-bottom: 5px;
        }

        .press-item .year {
            color: #999;
            font-size: 0.9em;
            margin-bottom: 15px;
        }

        .press-item .quote {
            font-style: italic;
            color: #555;
            margin: 8px 0 5px 0;
            line-height: 1.5;
        }

        .press-item .source {
            color: #666;
            font-size: 0.9em;
            margin-bottom: 15px;
        }

        .press-item .source strong {
            color: #333;
        }

        .press-item .award {
            color: #333;
            font-weight: 500;
            margin: 10px 0;
        }

        footer {
            background-color: #fff;
            color: #000;
            padding: 20px 40px;
            text-align: right;
            margin-top: 40px;
        }

        footer p {
            margin: 0;
            font-size: 0.85em;
        }

        @media (max-width: 768px) {
            .press-item {
                flex-direction: column;
            }

            .press-image {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>STEPHANIE SHUM</h1>
    </header>

    <nav>
        <a href="index.html">Welcome</a>
        <a href="headshots.html">Headshots</a>
        <a href="resume.html">Resume</a>
        <a href="video.html">Video</a>
        <a href="gallery.html">Gallery</a>
        <a href="press.html">Press</a>
        <a href="projects.html">Current and Upcoming Projects</a>
    </nav>

    <div class="container">
        <h2 class="page-title">Press</h2>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/gorgeous.jpg" alt="Gorgeous production photo">
            </div>
            <div class="press-content">
                <h3>Gorgeous</h3>
                <p class="year">2025</p>
                <p class="quote">"a sure-footed two-hander" with Shum bringing "humanity" to Jenny</p>
                <p class="source"><strong>Daily Herald</strong></p>
                <p class="quote">"deeply humanistic questions"</p>
                <p class="source"><strong>Chicago Reader</strong></p>
                <p class="quote">"verve and panache"</p>
                <p class="source"><strong>Newcity Stage</strong></p>
                <p class="quote">"energetic presence" and "honest character"</p>
                <p class="source"><strong>Chicago Theatre Review</strong></p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/one-party-consent.jpg" alt="One Party Consent production photo">
            </div>
            <div class="press-content">
                <h3>One Party Consent</h3>
                <p class="year">2025</p>
                <p class="quote">Shum "radiates rage and resentment"</p>
                <p class="source"><strong>Newcity Stage</strong></p>
                <p class="quote">"a volcano about to erupt"</p>
                <p class="source"><strong>Chicago Theatre Review</strong></p>
                <p class="quote">"powerhouse" performance</p>
                <p class="source"><strong>Around The Town Chicago</strong></p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/dogs.jpg" alt="Dogs production photo">
            </div>
            <div class="press-content">
                <h3>Dogs</h3>
                <p class="year">2024</p>
                <p class="quote">"powerhouse" performance</p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/revolution.jpg" alt="Revolution production photo">
            </div>
            <div class="press-content">
                <h3>Revolution</h3>
                <p class="year">2023</p>
                <p class="quote">"marvelous" and "endearing"</p>
                <p class="source"><strong>Chicago Sun-Times</strong></p>
                <p class="quote">Captures anxiety with "power and passion"</p>
                <p class="source"><strong>Broadway World, Chicago Theatre Review</strong></p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/small-world.jpg" alt="Small World production photo">
            </div>
            <div class="press-content">
                <h3>Small World</h3>
                <p class="year">2019</p>
                <p class="quote">"intense physical work" with determined optimism</p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/strange-heart-beating.jpg" alt="Strange Heart Beating production photo">
            </div>
            <div class="press-content">
                <h3>Strange Heart Beating</h3>
                <p class="year">2019</p>
                <p class="award">Joseph Jefferson Award Winner - Best Ensemble</p>
                <p class="quote">"electrifying" and "absolutely magnetic"</p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/plainclothes.jpg" alt="Plainclothes production photo">
            </div>
            <div class="press-content">
                <h3>Plainclothes</h3>
                <p class="year">2018</p>
                <p class="quote">Realistic monologue delivery</p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/second-skin.jpg" alt="Second Skin production photo">
            </div>
            <div class="press-content">
                <h3>Second Skin</h3>
                <p class="year">2018</p>
                <p class="award">5-star TimeOut Chicago rating</p>
                <p class="quote">Noted for intensity and "trademark intensity"</p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/seven-fights.jpg" alt="A Story Told in Seven Fights production photo">
            </div>
            <div class="press-content">
                <h3>A Story Told in Seven Fights</h3>
                <p class="year">2018</p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/harbur-gate.jpg" alt="Harbur Gate production photo">
            </div>
            <div class="press-content">
                <h3>Harbur Gate</h3>
                <p class="year">2018</p>
                <p class="quote">"especially strong" in complex team dynamic</p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/the-crucible.jpg" alt="The Crucible production photo">
            </div>
            <div class="press-content">
                <h3>The Crucible</h3>
                <p class="year">2017</p>
                <p class="source">Feature in <strong>AScene</strong></p>
                <p class="quote">Displayed "versatility" and "finesse" in multi-character roles</p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/mother-of-smoke.jpg" alt="Mother of Smoke production photo">
            </div>
            <div class="press-content">
                <h3>Mother of Smoke</h3>
                <p class="year">2017</p>
                <p class="quote">Praised for comedic and physical work</p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/kin-folk.jpg" alt="Kin Folk production photo">
            </div>
            <div class="press-content">
                <h3>Kin Folk</h3>
                <p class="year">2016</p>
                <p class="source"><strong>Daily Herald</strong> feature</p>
                <p class="quote">Portraying "painful vulnerability"</p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/circle-machine.jpg" alt="Circle-Machine production photo">
            </div>
            <div class="press-content">
                <h3>Circle-Machine</h3>
                <p class="year">2015</p>
                <p class="quote">Called "fiery" with "intense introspection"</p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/rewilding-genius.jpg" alt="reWILDing Genius production photo">
            </div>
            <div class="press-content">
                <h3>reWILDing Genius</h3>
                <p class="year">2014</p>
                <p class="quote">Praised for "mysterious, reticent" portrayal</p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/kate-and-sam.jpg" alt="Kate and Sam Are Not Breaking Up production photo">
            </div>
            <div class="press-content">
                <h3>Kate and Sam Are Not Breaking Up</h3>
                <p class="year">2013</p>
                <p class="award">5-star TimeOut Chicago rating</p>
                <p class="award">Joseph Jefferson nomination - Best New Work</p>
                <p class="quote">Delivering thoughts "at machine-gun pace"</p>
            </div>
        </div>

        <div class="press-item">
            <div class="press-image">
                <img src="images/press/alice.jpg" alt="Alice production photo">
            </div>
            <div class="press-content">
                <h3>Alice</h3>
                <p class="year">2013</p>
                <p class="quote">Character described as "defiantly likable"</p>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; Stephanie Shum 2025</p>
    </footer>
</body>
</html>
'''

if __name__ == '__main__':
    import os

    file_path = r'P:\Scripts\my-website\build\press.html'

    print(f"Updating {file_path}...")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(HTML_CONTENT)

    print("Done! Press page updated successfully.")
    print("\nKey changes made:")
    print("- Added flexbox layout for image + content side-by-side")
    print("- Added .press-image and .press-content containers")
    print("- Updated quotes and sources from reference site")
    print("- Added .award class for special recognitions")
    print("- Added responsive design for mobile")
    print("\nNote: You'll need to add the actual production images to:")
    print("  P:\\Scripts\\my-website\\build\\images\\press\\")
