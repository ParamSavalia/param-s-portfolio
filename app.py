from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# about_skills
@app.route('/')
def index():

#header-titles
    header_title_list = [
                            {'title': 'Home', 'href': '#home'},
                            {'title': 'About', 'href': '#about'},
                            {'title': 'Projects', 'href': '#projects'},
                            {'title': 'Contact', 'href': '#contact'}
        ]


#pages-titles
    title_list = ['About Me','Skills','My Projects','Contact Me']

#intro
    hero_intro = 'Hi, I\'m Param'
    hero_sub_intro = 'An IT professional with experience in Python, web development, and IT systems.'

#About
    aboutme = (
                    "Hey, I’m Param — a tech enthusiast and problem-solver living in Ottawa, "
                    "with a love for clean code and well-behaved networks. My journey started "
                    "with a diploma from Government Polytechnic and evolved into an advanced diploma "
                    "from Algonquin College in Computer Engineering Technology. Along the way, I dove "
                    "deep into the fascinating worlds of IT networking, backend development, and database architecture."
                    "These days, I work as a Support Engineer at <a href='https://www.checkpoint.com/about-us/'>Checkpoint Software Technologies</a>, "
                    "where I spend my time untangling network mysteries involving routers, switches, and firewalls. "
                    "I like to think of it as digital detective work — only with fewer trench coats and more command lines."
                    "Before that, I got hands-on with backend magic during a co-op at Parul Digital World,"
                    "where I built server-side logic, optimized databases, and learned the art of scalable, reliable systems."
                    "Whether I’m fixing a broken connection or designing a rock-solid backend, "
                    "my goal is simple: build smart, reliable tech that just works. When I'm not geeking out "
                    "over new tools or debugging lines of code, you’ll probably find me exploring the next "
                    "cool thing in tech or sketching out ideas for my next side project."
    )
    skill_list = [
        {'title': 'Languages', 'skills':'Java, Python, C/C++, SQL (Postgres), Angular'},
        {'title': 'Frameworks', 'skills':'WordPress, Packet Tracer, WireShark, VMWare, PuTTy, MS Azure, Virtual Box'},
        {'title': 'Operating System', 'skills':'Windows, Linux, QNX operating system'},
        {'title': 'Developer Tools','skills':'Git, GitHub Desktop, VS Code, Visual Studio, PyCharm, IntelliJ, Eclipse'},
        {'title': 'Database Tools', 'skills':'MongoDB, MySQL, FireBase, PostgreSQL'},
        {'title': 'Networking Concepts', 'skills':'DHCP, DNS, FTP, ARP, RARP, SSL, SSH, IPS, STP'},
        {'title': 'Networking Models', 'skills':'OSI, TCP/IP'}
    ]
    return render_template('index.html', hero_sub_intro=hero_sub_intro, hero_intro=hero_intro, aboutme= aboutme, title= title_list, header_title=header_title_list, about=skill_list)

#projects

# contact
@app.route('/contact', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Contact Form Submission: {name}, {email}, {message}")
        return redirect(url_for('home') + '#contact')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
