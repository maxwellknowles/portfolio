## Imports
import urllib
import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html

import urllib.request
from urllib.parse import urlparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import requests
from googlesearch import search

import matplotlib.pyplot as plt
from math import e

st.set_page_config(page_title="Maxwell Knowles Portfolio", page_icon=":100:", layout="wide",initial_sidebar_state="expanded")
with st.sidebar:
    choose = option_menu("Maxwell's Portfolio", ["Bio & Resume", "PM Product Example: Picker App", "PM Feature Example: Substitutions", "PM Hack Example: Glide Mobile App", "PM Data Example: Streamlit Analytics Web App", "Consulting: AR-Based NFT Gaming Startup", "Just for Fun: Curated Search", "Contact"],
                         icons=['house', 'kanban', 'kanban', '123', '123', 'activity', 'apple', 'archive'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#BBBBBD"},
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#BBBBBD"},
    }
    )

if choose == 'Bio & Resume':
    st.title('Maxwell Knowles: Bio & Resume')
    st.write("Hey there! Welcome to my portfolio of projects and tools I created with Python and Streamlit.")
    st.write("I made this web app so friends, companies, and recruiters alike could see what I've been up to as a product manager, fan of data science, music maker, and javelin thrower.")
    col_photo, col_about = st.columns(2)
    with col_about:
        st.header('About')
        st.write("I completed my undergraduate studies as an Edward J. Sexton Fellow of Philosophy, Politics, and Economics at Claremont McKenna College in 2020 before joining Zero as its eighth full-time team member. Since starting in May of 2020, I've focused on elevating Zero's tech and data visibility, collaborating regularly with engineering, data science, warehouse and fleet operations, growth, and business operations. I'm currently taking coursework in entrepreneurship and venture capital at Claremont Graduate University and competing in the javelin throw, continuing to work in Product along the way.")
        st.write("Thanks for taking the time to learn a bit more about me!")
    with col_photo:
        st.image("https://github.com/maxwellknowles/portfolio/raw/main/_89A6473_DxO%20.jpg")
    resume = "https://github.com/maxwellknowles/portfolio/raw/main/Maxwell_Knowles_Resume_2022.pdf"
    st.write("[Download Resume](%s)" % resume)
    with st.expander("See Resume"):
        st.image("https://github.com/maxwellknowles/portfolio/raw/main/resume.png")

    st.header('Work Experience')
    st.subheader("Zero Grocery")
    st.markdown("**Product Manager** _(August 2021 - March 2022)_")
    with st.expander("See details"):
        st.write("• Scaffolded and led release strategy for Zero’s first delivery windows option, allowing Zero to offer the feature on selected days and regions to ensure a safe, cost-sensitive, and customer-pleasing rollout")
        st.write("• Led development of substitutions feature, winning back 20 percent of potential out-of-stock revenue loss")
        st.write("• Pulled and manipulated Shopify and inFlow data via API GET endpoints and Python, writing and automating scripts in GCP that surfaced refund, out-of-stock, demand forecasting, and alcohol data")
        st.write("• Stitched GCP, Google Sheets, Python, and Streamlit together to release Zero’s most comprehensive analytics web app, providing insight into item popularity, order metrics, order location, and more")

    st.markdown("**Associate Product Manager** _(May 2020 - July 2021)_")
    with st.expander("See details"):
        st.write("• Led design and hands-on implementation of a gig delivery system built on k-means clustering, dropping Zero’s cost per delivery by 50 percent, automating driver signup, and increasing driver cohort 10x")
        st.write("• Oversaw development and release strategy for new picker app — based on a successful low-code prototype — decreasing average pick time per order by 40 percent in its first month of implementation")
        st.write("• Leveraged GCP, Python, and MongoDB data to write and automate scripts that surfaced fulfillment, cancellation, referral, demand forecasting, and live out-of-stock data, supporting multiple departments")

    st.subheader("Truepill")
    st.markdown("**Business Intern** _(February 2020 - May 2020)_")
    with st.expander("See details"):
        st.write("• Referenced drugs.com, clinicaltrials.gov, and individual company websites to compile data on 1000 drugs based on trial phase, collaborating with the Director of Business Development")
        st.write("• Researched Crunchbase and other publications to identify rising startups in the life sciences space, compiling a list of potential business leads based on type and phase of drugs in progress")

    st.subheader("Tuesday Capital")
    st.markdown("**Summer Analyst** _(June 2019 - August 2019)_")
    with st.expander("See details"):
        st.write("• Studied Crunchbase data, McKinsey reports, Forbes articles, and other sources to research, analyze, and map competitive landscapes for six different markets to inform investors taking new deals")
        st.write("• Used Google Sheets and Data Studio to conduct data entry and analysis on 27 drugs as an “extern” at Truepill, a Series A startup, compiling insights to leverage for new business with drug manufacturers")
        st.write("• Completed various ad hoc tasks, from taking notes on startup pitches to categorizing thousands of Affinity entries to facilitating social engagements and developing manager’s personal brand")
        st.write("• Employed extensive tagging and varied content to grow LinkedIn following by 50 percent and reach twice the Twitter impressions (775K) in three months than in the four years prior combined, all organically")

    st.header("Skills & Tools") 
    with st.expander("Technical"):
        st.write("Python (proficient), R (proficient), MongoDB (proficient), Excel/Google Sheets (proficient), Google Analytics (proficient), Streamlit (proficient), Glide Apps (proficient), SQL (basic)")
    with st.expander("Management & Design"):
        st.write("Scrum, Notion, Jira, Linear, Trello, Miro, Whimsical, Figma")
    with st.expander("Interests"):
        st.write("Music, Poetry, Philosophy, Entrepreneurship, Comedy, Populism")
        
    st.header('Education')
    st.subheader("Claremont Graduate University")
    st.markdown("**Certificate in Entrepreneurship** _(May 2022)_")
    with st.expander("Selected coursework"):
        st.write("Entrepreneurial Finance, Startup Business Models")
    st.subheader("Claremont McKenna College")
    st.markdown("**BA in Philosophy, Politics, and Economics** _(December 2020)_")
    with st.expander("Senior Thesis"):
        thesis = "https://scholarship.claremont.edu/cmc_theses/2502/"
        st.write("[_Populism: An Exploration into the American Case Through the Academic Literature, Data Analysis, and Fiction_](%s)" % thesis)
        st.write("The twenty-first century has seen a rise in populist leadership and rhetoric throughout the globe, with the United States standing as one powerful case. This thesis hopes to develop the “story” of populism from multiple perspectives, attempting to not only inform but change the way we approach the populist movement in America, and perhaps, the world. In Part I, I summarize and blend much of the core literature written on populism and economic change, developing the story that populism in America today has its roots in the significant techno-economic and cultural paradigmatic shifts of the 1970s. Social media and an evolving political philosophy, particularly among the youth, are also explored. In Part II, I iterate multiple predictive data models using roughly 20 dimensions of democratic and economic life in the United States as independent variables, with different definitions of populism as the dependent variable. I find — counter to what the aforementioned literature might imply — that increasing unemployment is negatively correlated with populist leadership (at a significance level of 0.05, no less), while the “civil society organization participatory environment” and “social class equality in civil liberty” variables are positively correlated, corresponding conceptually with the literature. Finally, Part III is a creative work — The Mind of Demos — in which a fictional college student allegorizes the rise and nature of populism in six cantos, complete with two fictional commentaries and a forward by a fictional professor from the future.")
    with st.expander("Selected coursework"):
        st.write("The Politics of the Gig Economy, Data Science & Statistical Learning, The Idea of Poetry")

    st.header("Athletics") 
    st.subheader("CMS Track & Field")
    st.markdown("**Javelin Thrower** _(January 2017 - Present)_")
    with st.expander("See details"):
        st.write("• Returned to Claremont for the 2022 season to compete with final year of NCAA athletic eligibility, ranked #4 in school history in the javelin throw and a member of the CMS Wall of Fame")
        st.write("• Voted Men’s Team Captain and nominated for CMS Junior Athlete of the Year in 2019")
        st.write("• SCIAC Champion (2019), USTFCCCA All-West Region honoree (2019), USTFCCCA All-Academic (2019), and NCAA Qualifier, ranking 12th in DIII nationally in 2019")

    st.header("Music") 
    st.markdown("**Singer-Songwriter & Producer** _(November 2020 - Present)_")
    st.write("Write and record indie-alternative music, both instrumental and vocal :)")
    spotify = "https://open.spotify.com/artist/2p2YiVrDP0scQefeefDqCO?si=b7X6T-Y1Q6eG6DwsPTKbyg"
    st.write("[Visit my Spotify!](%s)" % spotify)

if choose == "PM Product Example: Picker App":
    st.title("PM Product Example: Picker App")
    st.header("Transforming Zero's Picker App: From Low-Code Prototype to React App")
    st.subheader("Some Context")
    st.write("Zero Grocery opened a central distribution warehouse in Fresno, CA and spent a few months experimenting with picking all orders in Fresno, then sending these orders to the local markets (the Bay Area and Los Angeles). The warehouse was massive, placing incredible strain on a picker physically and dramatically slowing down Zero's average pick time per order.")
    st.subheader("The Prototype")
    st.write("With sparse Engineering resources, I was asked to lead a small trio (consisting of myself, a data scientist, and an operations associate) to build a functional prototype that we could iterate and use to collect data before working with Engineering on a proper build. After a few hours considering our options, we landed on what was dubbed the 'Mongo loop' approach.")
    st.write("I asked our data scientist to write a Python script that pulled order data from MongoDB, which I then modified to populate a Google Sheet directly. The operations associate had mapped out the warehouse to assign items a 'grid' position in the warehouse to order steps more efficiently. This grid data could be associated with each item found in our data scientist's script. I then formatted the spreadsheets so that a Glide app could be used to interact with the data, with picker actions providing us with the actual picked levels for items listed in orders. After picking with the app was concluded for the day, a single spreadsheet could be read from using a second Pytho script, modifying the relevant orders in MongoDB appropriately.")
    st.write("Although quite hacky, this prototype was functional enough to pick dozens of orders. We could see the benefits of a grid position, take notes on UI/UX, and log pick times with orders of different sizes. This built conviction within the Product, Operations, and Engineering teams, leading to a full build with software engineers.")
    picker_app_prototype = "https://youtu.be/ZtvJVsx77V4"
    st.video(picker_app_prototype)
    st.subheader("The Picker App Build")
    st.write("With use of the prototype showing significantly lower pick times, I was asked to work with two software engineers (one BE and one FE) to go about a proper build. This app was optimized for picking on a tablet and manager assignment on desktop. We implemented the major features that proved so useful in the prototype — dividing up orders into cold and dry components and providing grid position — and added in color coding by pick status to help pickers visually. Further, we built with future features in mind, including substitutions, so implementation could be fast and effective.")
    st.subheader("Outcomes")
    st.markdown("_Picker accuracy remained strong, **average pick times were cut by 40%**, and we were able to easily layer in substitution as a feature months later_.")
    picker_app_react = "https://youtu.be/qNePEABFlXU"
    st.video(picker_app_react)

if choose == "PM Feature Example: Substitutions":
    st.title("PM Feature Example: Substitutions")
    st.header("An Exercise In Adapting")
    st.subheader("Some Context")
    substitution_study_interviews = "https://github.com/maxwellknowles/portfolio/raw/main/substitutions/Screen%20Shot%202022-03-02%20at%208.22.39%20PM.png"
    substitution_study_plan = "https://github.com/maxwellknowles/portfolio/raw/main/substitutions/Screen%20Shot%202022-03-02%20at%208.39.02%20PM.png"
    substitution_study_prd_prep = "https://github.com/maxwellknowles/portfolio/raw/main/substitutions/Screen%20Shot%202022-03-02%20at%208.39.55%20PM.png"
    miro = "https://github.com/maxwellknowles/portfolio/raw/main/substitutions/Screen%20Shot%202022-02-28%20at%201.35.05%20PM%20(1).png"
    competitors = "https://github.com/maxwellknowles/portfolio/raw/main/substitutions/Screen%20Shot%202022-02-28%20at%201.35.29%20PM%20(1).png"
    st.write("In the grocery delivery market, offering substitutions for out of stock (OOS) products is commonplace. It can make customers happier and preserves revenue for the stores and delivery services. The way individual players have decided to attack this problem, however, varies. At Zero, we wanted to know how we could transform our approach at the time — a consumer opt-in for best-effort substitutes — into something truly delightful on the consumer side while still being practical operationally.")
    col_plan, col_plan_words = st.columns(2)
    col_interview_words, col_interview = st.columns(2)
    col_prd, col_prd_words = st.columns(2)
    with col_plan:
        st.image(substitution_study_plan)
    with col_plan_words:
        st.subheader("The Plan")
        st.write("I worked with Zero's user researcher at the time to establish a plan of attack for rapid research. We would interview customers and Zero Operations leadership, as well as conduct some competitive market research to see what options and UI/UX were predominate.")
        st.image(competitors)
        st.caption("A market landscape matrix (the goal was to enter the upper-left quadrant).")
    with col_interview_words:
        st.subheader("The Execution")
        st.write("We successfully completed interviews with eight Zero customers, an operations manager, and a warehouse lead, identifying pain points in the user experience on our website and with our fulfillment tech as it stood then. We had the following main takeaways...")
        st.write("**For Zero Operations**")
        st.write("• Pickers needed to have defined lists of what could or could not be substituted for a given product (a _data_ issue)")
        st.write("• It wasn't obvious to the folks checking picker work that an item had been substituted (a _UI/UX_ issue).")
        st.write("• There was concern around how a customer's subtotal may fluctuate with substitutions (an _ethics_ issue).")
        st.write("**For Zero Customers**")
        st.write("• No email or SMS notification when substitutions happen (a _communication_ issue)")
        st.write("• Many customers weren't even seeing or engaging with the substitution checkbox in our current checkout experience (a _UI/UX_ issue)")
        st.write("• Many customers complained about the quality or relevancy of the items pickers had chosen as substitutes (a _picking_ issue)")
        st.write("• Some customers, especially those with dietary restrictions, cared about curating their substitutions, while others simply wanted to say 'YES' or 'NO' (an _adaptability_ issue)")
    with col_interview:
        st.image(substitution_study_interviews)
        st.caption("An interview database we made in Notion.")
        st.image(miro)
        st.caption("Little notes from customer interviews were made in Miro, allowing us to cluster the notes thematically and distill major takeaways.")
    with col_prd:
        st.image(substitution_study_prd_prep)
        st.caption("A cut from a 'PRD Prep' doc with research and product recommendations. I drafted, refinded, and shared this doc to get stakeholder buy-in before moving forward with engineering.")
    with col_prd_words:
        st.subheader("Our Recommendation")
        st.write("We ultimately landed on a 'paved path' approach (referring to how it guided both customers and pickers) to substitutions, providing a binary YES/NO option for customers that would make each item in a _defined list of potential substitutions_ visible for pickers on their end, **_but_** if a customer cared to narrow this list, they could simply de-select one or multiple options.")
    st.subheader("Adapting & Winning Back Revenue")
    st.write("As often happens with an early-stage startup, priorities changed and substitutions needed to be pushed off the roadmap for months. The website needed other attention and Zero operations were evolving rapidly as we scaled.")
    st.write("As the dust settled, however, out-of-stocks continued to be a troublesome issue and we weren't capturing the revenue we could be. This led me to work with a software engineer on a rapid, de-scoped version of our substitutions recommendation, bringing back the default YES/NO for customers, but associating a list of one to four substitutions for each eligible item that would be visible on the picker's end (preventing poor substitutions, the primary customer issue). The work could be boiled down to some data model changes and fairly light additions to the picker app.")
    st.write("Although continuing to develop the customer-facing experience is important, this was another example of our Product and Engineering teams adapting quickly but thoughtfully. The de-scoped build took a matter of days and allowed us to win back 20 percent of the revenue we would have otherwise lost from out-of-stocks.")

if choose == "PM Hack Example: Glide Mobile App":
    st.title("PM Hack Example: Glide Mobile App")
    st.write("During my time working in Product at Zero Grocery (an early-stage startup), I quickly learned the value of being able to rapidly spin up low or no-code solutions for ad hoc and isolated issues in order to keep our lean team of software engineers on our established roadmap. Engineering at a startup is often a precious resource, and I have embraced the challenge of both becoming a more technical PM and utilizing low-code resources — such as Streamlit and Glide Apps — to solve business problems.")
    st.header("Tool: Stock Verification")
    st.subheader("Purpose")
    st.write("Allow operations and merchandising leads to verify stock levels for items marked out-of-stock as pickers fulfill orders.")
    st.subheader("How It Works")
    st.write("I wrote a Python script that filtered orders on their packing status, checked each item in each relevant order for a 'not_packaged' attribute, then uploaded a dataframe of out-of-stock items in in-progress orders to Google Sheets. I deployed the script in GCP, then used the Google Cloud Scheduler to automate running the script every 5 minutes, allowing our team to adapt in real-time. Finally, I used one of my favorite no-code solutions, Glide Apps, to create an easy mobile UI for teammates to find and sort the relevant data. Glide treats spreadsheets like a database, so as long my GCP function continued to update the data in Google Sheets, app users would have a constant flow of accurate and actionable information.")
    st.subheader("Screen Recorded Walkthrough")
    st.video("https://youtu.be/NEJvjzBdl9k")
    glide = "www.glideapps.com"
    st.caption("Find more information on Glide [here](%s)" % glide)

if choose == 'PM Data Example: Streamlit Analytics Web App':
    st.header("PM Data Example: Streamlit Analytics Web App")
    analytics = "https://share.streamlit.io/maxwellknowles/analytics_web_app/main/analytics.py"
    st.write("To click through an anonymized version of the analytics web app, click [here](%s)!" % analytics) 
    st.subheader("Purpose")
    st.write("To create the most comprehensive place for different teams (Operations, Growth, Merchandising, etc.) to come and engage with data from three Shopify sites and inFlow.")
    st.subheader("How It Works")
    st.write("I wrote a Python script that pulled in data from spreadsheets (which were populated with GCP functions that interacted with Shopify and inFlow at set intervals, preventing us from hitting API call limits). I then used the Streamlit library to present this data in a user-friendly manner, organizing the data thematically and implementing charts, maps, rankings, and k-means clustering.")
    st.subheader("Screen Recording")
    st.video("https://youtu.be/vn3SJHaw4tM")

if choose == "R Analysis Samples":
    st.title("Data-Intensive Work")
    st.header('Churn Analysis Report Coded in R')
    with st.expander("See Report"):
        st.image("https://github.com/maxwellknowles/portfolio/raw/main/CancellationReport1.png")
        st.image("https://github.com/maxwellknowles/portfolio/raw/main/CancellationReport2.png")
        st.image("https://github.com/maxwellknowles/portfolio/raw/main/CancellationReport3.png")
        st.image("https://github.com/maxwellknowles/portfolio/raw/main/CancellationReport4.png")
    st.header('Renewal Mill Mock Vendor Report Coded in R')
    with st.expander("See Report"):
        st.image("https://github.com/maxwellknowles/portfolio/raw/main/renewal1.png")
        st.image("https://github.com/maxwellknowles/portfolio/raw/main/renewal2.png")
        st.image("https://github.com/maxwellknowles/portfolio/raw/main/renewal3.png")

if choose == "Consulting: AR-Based NFT Gaming Startup":
    #-------------------------
    #Main Menu Sidebar -- CONFIG
    #-------------------------
    eikona_choice = option_menu("Consulting: AR-Based NFT Gaming Startup", ["Industry User Growth", "Tokenomics & Business Model"],
                        icons=['activity', '123'],
                        menu_icon="calculator", default_index=0, orientation="horizontal",
                        styles={
    "container": {"padding": "5!important", "background-color": "#BBBBBD"},
    "icon": {"color": "white", "font-size": "25px"}, 
    "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
    "nav-link-selected": {"background-color": "#BBBBBD"},})

    ##data
    coinbase_users_historic = pd.read_csv("https://raw.githubusercontent.com/maxwellknowles/eikona/main/coinbase_users.csv")
    pokemongo_users = pd.read_csv("https://raw.githubusercontent.com/maxwellknowles/eikona/main/pg_users.csv")

    #####
    ##Variables/Default values - PreCache
    #####

    ###Calculating TPM
    interval_of_users = 50
    p_coefficient = float(0.006)
    q_coefficient = float(0.410)

    #Define Bass Diffusion Model Function first here for efficiency
    def get_bass_model(p, q, M, period = 30):

        # Initializing the arrays
        A = [0] * period
        R = [0] * period
        F = [0] * period
        N = [0] * period

        # One important thing to note, is that the time period we start from is t = 0.
        # In many articles, you will see time starting from t = 1. They are both the
        # same for all intents and purposes. Starting with t = 0 makes life easier in
        # python, as indexing in python starts from 0 too.

        # We start with A(0) =0, and build up the values for t = 0 from the equations
        # formulated
        A[0] = 0
        R[0] = M
        F[0] = p
        N[0] = M*p

        # Recursion starts from next time step
        t = 1

        # Creating a helper function for recursion
        def get_bass_model_helper(A, R, F, N, t):

            # If we have reached the final period, return the values
            if t == period:
                return N, F, R, A
            else:

                # Else, just compute the values for t
                A[t] = N[t-1] + A[t-1]
                R[t] = M - A[t]
                F[t] = p + q * A[t]/M
                N[t] = F[t] * R[t]

                # compute values for the next time step
                return get_bass_model_helper(A, R, F, N, t+1)

        N, F, R, A = get_bass_model_helper(A, R, F, N, t)

        # Converting to numpy arrays and returning.
        return np.array(N), np.array(A)

    #-------------------------
    #Business Model
    #-------------------------
    if eikona_choice == "Industry User Growth":
        eikona_link = "eikona.art"
        eikona_streamlit_app = "https://share.streamlit.io/eikona-patunga/eikona-analytics/main/eikona_pitch.py"
        st.subheader("_Some Context_")
        st.write("Eikona — [a startup](%s) working at the nexus of AR gaming and NFTs — is currently pitching to incubators and early-stage investors. I've provided hours in product and strategy on the project, collaborating with the founder on this Streamlit app to serve as one tool in developing and visualizing Eikona's tokenomics and business model." % eikona_link)
        st.write("You can see the latest Streamlit app for Eikona [here](%s)." % eikona_streamlit_app)
        st.title("Industry User Growth")
        st.header('_Crypto & AR-Gaming_')

        col1, col2 = st.columns(2)

        #################
        ###Industry Growth
        # Coinbase YoY -- millions
        ###Changeables/Sliders:
        # - Estimated YoY Growth% from 2022 Onward
        #################

        with col1:
            cb_historic_rate = ((coinbase_users_historic['Coinbase Users'][len(coinbase_users_historic)-1]-coinbase_users_historic['Coinbase Users'][0])/coinbase_users_historic['Coinbase Users'][0])/8
            cb_historic_rate = str(round(cb_historic_rate*100))+" %"
            st.write('Coinbase Average Annual User Growth (2014-2021):', cb_historic_rate)
            cb_growth = st.slider('Estimated YoY Growth (%) for Coinbase Users from 2022 Onward...', -100, 1000, 100)
            cb_growth = cb_growth*0.01
            l   = []
            for i in range(1,5):
                year = str(2021+i)
                cb_users = round(56*(1+cb_growth)**i)
                tup=(year, cb_users)
                l.append(tup)
            cb_projected = pd.DataFrame(l, columns=['Year','Coinbase Users'])
            coinbase_users = coinbase_users_historic.append(cb_projected, ignore_index=True)
            l = []
            for i in coinbase_users.iterrows():
                year = datetime.strptime(str(i[1]['Year']),"%Y")
                cb_users = i[1]['Coinbase Users']
                tup=(year, cb_users)
                l.append(tup)
            coinbase_users = pd.DataFrame(l, columns=['Year','Coinbase Users'])
            coinbase_users = coinbase_users.set_index('Year')


            st.subheader('Coinbase Users (in millions)')
            st.line_chart(coinbase_users)

        #################
        ###Industry Growth
        # Pokemon YoY -- millions
        ###Changeables/Sliders:
        # - Estimated YoY Growth% from 2022 Onward
        #################

        with col2:
            pg_historic_rate = ((pokemongo_users['PG Users'][len(pokemongo_users)-1]-pokemongo_users['PG Users'][1])/pokemongo_users['PG Users'][1])/4
            pg_historic_rate = str(round(pg_historic_rate*100))+" %"
            st.write('Pokemon GO Average Annual User Growth (2017-2020):', pg_historic_rate)
            pg_growth = st.slider('Estimated YoY Growth (%) for Pokemon GO Users from 2021 Onward...', -100, 1000, 40)
            pg_growth = pg_growth*0.01
            l = []
            for i in range(1,6):
                year = str(2020+i)
                pg_users = round(166*(1+pg_growth)**i)
                tup=(year, pg_users)
                l.append(tup)
            pg_projected = pd.DataFrame(l, columns=['Year','PG Users'])
            pokemongo_users = pokemongo_users.append(pg_projected, ignore_index=True)
            l = []
            for i in pokemongo_users.iterrows():
                year = datetime.strptime(str(i[1]['Year']),"%Y")
                pg_users = i[1]['PG Users']
                tup=(year, pg_users)
                l.append(tup)
            pokemongo_users = pd.DataFrame(l, columns=['Year','PG Users'])
            pokemongo_users = pokemongo_users.set_index('Year')

            st.subheader('Pokemon GO Users (in millions)')
            st.line_chart(pokemongo_users)

        #-------------------------
        ###Business Model Sidebar -- Calculating TPM

        st.title('Bassian Diffusion: Exploring the Market Opportunity')

        col3, col4 = st.columns(2)

        with col3:
            image = "https://github.com/maxwellknowles/portfolio/raw/main/Diffusion-of-Innovation.png"
            st.image(image)

        with col4:
            st.write('**Bassian Diffusion of Innovaton Adoption** is a widely-accepted sociological phenomenon, successfully modeling the rate of adoption or growth for everything from Twitter trends to users of new devices.')
            st.write("Eikona is keen on understanding how the crypto space will evolve, what the ultimate market opportunity is, and how our unique positioning might unlock the most aggressive share of that market opportunity. As an exercise to evaluate crypto adoption, we've set the default values of the _p-coefficient_ (adoption), _q-coefficient_ (imitation), and industry size of the Bass model below to match the user adoption of Coinbase through 2021.")
            st.write("Based on this analysis, we believe we are only now transitioning from the **_early adopters_** to the **_early majority_**, making Eikona's method and mission of tackling widespread adoption through a _safe_, _simple_, and _fun_ experience not only unique, but _**timely**_. We are built for this moment.")
        
        st.subheader("Using Coinbase users as a proxy for crypto adoption in light of Bass diffusion...")
        col5, col6 = st.columns(2)

        with col5:
            #Setting Up Sliders
            industry_size = st.slider('Select Industry Size by 2040 (IN BILLIONS)', min_value = 0.1, max_value = 5.5,value = 1.0, step = 0.01)

            p_coefficient = st.slider('P Coefficient: Innovation', min_value = 0.001, max_value = 0.050, value = p_coefficient, step = 0.005)
            q_coefficient = st.slider('Q Coefficient: Imitation', min_value = 0.250, max_value = 0.550, value = q_coefficient, step = 0.005)
            period = st.slider('Period of time to predict until:', min_value = 10, max_value = 100, value = 25, step = 1)
            industry_size = 1000000000 * industry_size

            #col1 = st.columns(1)
            #with col1:
        
        with col6:

            fig = plt.figure()
            ax = plt.gca()

            #Pull in historic Coinbase user data and reformat for Bass graph
            coinbase_users_historic["Lifetime"] = coinbase_users_historic['Year']-2014
            coinbase_users_historic = coinbase_users_historic.drop("Year", 1)
            coinbase_users_historic["Users"] = coinbase_users_historic['Coinbase Users']*1000000
            coinbase_users_historic = coinbase_users_historic.drop("Coinbase Users", 1)
                
                #Plot Coinbase user data
            ax.plot(coinbase_users_historic['Lifetime'], coinbase_users_historic['Users'],'x', markersize=5)

                #Calling the function to get the new models
            N, A = get_bass_model(p_coefficient, q_coefficient, M=float(industry_size), period = period)
                
                #Creating Periods
            t = list(range(0, period))

                #Plotting Data and changing size of points
            ax.plot(t, N, 'o', markersize = 4)
                
                #Give it a cleaner look and remove the spines
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)

                # Setting label and title
            ax.set_title('Adoption Count for p = {} and q = {}'.format(p_coefficient, q_coefficient))
            ax.set_ylabel("New Customers")
            ax.set_xlabel("Industry Lifetime (y)")

                # Creating a clean layout
            fig.tight_layout()

            st.pyplot(fig)

            users_t = coinbase_users_historic['Users'][7]
            t = coinbase_users_historic['Lifetime'][7]
            m = users_t * (p_coefficient/(p_coefficient+q_coefficient)**2) * (((1 + (q_coefficient/p_coefficient) * (e ** -(p_coefficient + q_coefficient)*t))**2) / (e ** -(p_coefficient+q_coefficient)*t))
            

    if eikona_choice == "Tokenomics & Business Model":
        st.header("Tokenomics & Business Model")

        #initial values

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Levers")
            #initial values
            total_value = st.slider('Total Market Cap ($) Starting in Reserve: ', min_value = 100000, max_value = 5000000, value = 100000, step = 100000)
            total_coin = st.slider('Initial Circulating Supply of $EKO', min_value = 1000000000, max_value = 1000000000000, value = 1000000000, step = 1000000000)
            percent_coin_owned = total_coin
            #parameters
            initial_people_involved = st.number_input('Number of initial players: ', min_value = 1, max_value = 100000000, value = 10000, step = 250)
            user_growth_rate = st.slider('Rate of User Growth/Month: 0.01 is equal to 1 percent of initial users', min_value = 0.01, max_value = 10.0, value = 0.5)
            avg_min_month = st.slider('Average Minutes Walked in AR/Month: ', min_value = 0, max_value = 600, value = 300, step = 10)
            st.write('_Equivalent to ' + str(float(avg_min_month/60)) + ' hours or ' + str(avg_min_month*60) + ' seconds_')
            rate_per_sec_AR = st.slider('$EKO generated each second in AR ad-compatible space: ', min_value = 0.001, max_value = 5.0, value = 0.01)
            x = (avg_min_month*60)*rate_per_sec_AR
            rate_of_generation = x #rate of $EKO per month being generated

            people_involved = initial_people_involved

            #days = 1000
            #total_coin = total_coin+people_involved*rate_of_generation*days
            #v1 is the value that our coin worth
            v1 = total_value*(percent_coin_owned/total_coin)
            #v2 is the value of a single coin
            v2 = v1/percent_coin_owned

            #m is the amount of months it takes for The Reserve to be worth 1 dollar
            m = (total_value/1000*percent_coin_owned-percent_coin_owned)/(rate_of_generation*people_involved*100)


            fig = plt.figure()
            ax = plt.gca()
            uot_line = plt.gca()



            v_ = []
            uot = []
            l = []
            days_simulated = int(m)
            for i in range(days_simulated):
                month = i
                total_coin = percent_coin_owned+(initial_people_involved + (initial_people_involved * user_growth_rate))*rate_of_generation*i
                v = total_value*(percent_coin_owned/total_coin)
                uot_ = (initial_people_involved+(initial_people_involved * user_growth_rate*i))
                tup = (month, uot_, v)
                uot.append(uot_)
                l.append(tup)
                v_.append(v)


        with col2:
            st.subheader("Visualizing Tokenomics")
            ax.plot(range(days_simulated),v_, label = 'Coin to users travellig the quota in AR over time')
            uot_line.plot(range(days_simulated), uot, label = 'Number of Impressionable users over time')
            plt.plot(60, uot[60], marker="x", label = 'The number of players at 5 years in: ' + str(uot[60]), markeredgecolor="red", markerfacecolor="green")
            plt.plot(60, v_[60], marker="x", label = 'The value of the coin at 5 years in: ' + str(v_[60]), markeredgecolor="blue", markerfacecolor="blue")
            plt.xlabel("Months to People-Owned Currency")
            plt.ylabel("Reserve Value")
            plt.legend()
            plt.xlim(4,100)
            #plt.ylim(10000, 10000000)
            #plt.ylim = (initial_people_involved, 1000000)
            #start, end = ax.get_ylim()
            #plt.yticks(np.arange(start, end, 1000000000))

            fig.tight_layout()
            st.pyplot(fig)

            st.write('What this shows is the amount of coin we own over time vs. The ammount of concurrent players holdings(x) plotted against the number of months at those settings it will take before The Reserves initial market supply loses value to 1$')

        st.header("The Business Model")
        col3, col4 = st.columns(2)
        with col3:
            uot = pd.DataFrame(l, columns = ['Year', 'Users', '$EKO Value'])
            st.subheader('Toggle Revenue Basics')
            #cost_mint = st.slider('Estimated Cost of User to Mint ($)...', 0.00, 5.00, 0.25, 0.05)
            #server_cost = st.slider('Estimated Server Costs (Per User in $)...', 0.00, 1.00, 0.10, 0.01)
            price_mint = st.slider('Estimated Price for User to Mint ($USD)...', 0.00, 10.00, 5.00, 0.25)
            #conversion_rate = st.slider('Estimated Share of Users Who Mint (%)...', 0, 100, 50)
            #conversion_rate = conversion_rate*0.01
            ar_ad_cpm = st.slider('Estimated Avg Number of Exchanges In-Game', 0, 50, 10)
            transaction_cost = st.slider('Transaction Fee ($USD)...', 0.00, 5.00, 0.25, 0.05)

        with col4:
            st.subheader("Eikona Game Revenue & Ad-Eligible Users By Year")
            l = []
            for i in uot.iterrows():
                month = float(i[1]['Year'])
                users = i[1]['Users']
                coin = i[1]['$EKO Value']
                revenue = users*price_mint + users*ar_ad_cpm*transaction_cost
                tup=(month, users, coin, revenue)
                l.append(tup)
            eikona_business = pd.DataFrame(l, columns=['Month','Users','$EKO Value', 'Revenue ($USD)'])
            eikona_business = eikona_business.set_index("Month")
            eikona_user_and_revenue = eikona_business[['Users', 'Revenue ($USD)']]
            eikona_user_and_coin = eikona_business[['Users', '$EKO Value']]
            st.area_chart(eikona_user_and_revenue)
        
        st.subheader("Eikona inching toward people-owned currency only comes with growth in valuable AR ad-eligible userbase...")
        st.area_chart(eikona_user_and_coin)

if choose == "Just for Fun: Curated Search":
    st.title("Just for Fun: Curated Search")
    st.write("This is a simple little tool that I created when I started practicing scripting in Python. I realized I was frustrated when I searched topics in business, tech, politics, or finance, because a) I didn't know how long the articles were before clicking and b) I couldn't narrow the results down to specific sites I liked.")
    l = ["www.wsj.com", "www.huffpost.com","www.gutenberg.org","scholar.google.com","hbr.org","scholar.harvard.edu",
        "www.theguardian.com","www.bloomberg.com","www.nytimes.com","www.forbes.com","angel.co",
        "www.businessinsider.com","www.crunchbase.com","www.entrepreneur.com","techcrunch.com","hbr.org",
        "www.mckinsey.com","stanford.edu","www.britannica.com","plato.stanford.edu","www.wordstream.com",
        "www.inc.com","www.economist.com","medium.com","www.investopedia.com","www.gutenberg.org",
        "www.lifehack.org","mashable.com", "www.fastcompany.com"]
    website_list = pd.DataFrame(l, columns=['Websites'])
    selection = st.multiselect("Choose the sites you prefer to be in your recommended list (if you don't have a preference, just leave blank and it'll filter using my list of favorite sites)",website_list['Websites'])
    web_list = pd.DataFrame(selection, columns=['Websites'])
    if len(web_list) == 0:
        web_list = website_list
    else:
        pass
    reading_speed = 200
    def myfunction(query):
        st.subheader('Getting Google search results and length of articles...')

        # to search
        data = pd.DataFrame([])
        for j in search(query, tld="com", num=20, stop=20, pause=2):
            r = requests.get(j)
            soup = BeautifulSoup(r.text, features="html.parser")
            for script in soup(["script", "style"]):
                script.extract()
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            text_list = text.split()
            st.write(f"{j} {len(text_list)} words or roughly {len(text_list)//reading_speed} minutes")
            words = len(text_list)
            minutes = words//200
            base0 = urlparse(j)
            base1 = base0[1]
            data = data.append(pd.DataFrame({'URL': j, 'Word Count': words, 'Reading Time': minutes, 'Base URL': base1}, index=[0]), ignore_index=True)
        else:
            pass
        #print(f"Total: {words} words or roughly {minutes} minutes")
        data = data.drop_duplicates(subset = ["Word Count"])
        data = data.reset_index(drop=True)
        
        st.subheader('Here are your recommendations...')
        curated = pd.DataFrame([])
        for i in range(0,len(data)):
            if data['Base URL'][i] in web_list.values:
                curated = curated.append(pd.DataFrame({'URL': data['URL'][i],'Word Count':data['Word Count'][i], 'Reading Time': data['Reading Time'][i], 'Base URL':data['Base URL'][i]}, index=[0]), ignore_index=True)
                st.write(f"{data['URL'][i]} is {data['Word Count'][i]} words long, with an estimated reading time of {data['Reading Time'][i]} minutes")
            else:
                pass
        
        #if len(curated) == 0:
        #    st.write("Your selected sites weren't in the top search results — try adding sites to widen your recommendations :)")
        #else:
        #    pass
    
    query = st.text_input('Your search...')
    reading_speed = st.slider('How many words do you read per minute?', 50, 500, 200)
    if st.button('Submit query'):
        if len(query)>0:
            st.write('Query in progress...')
            query = str(query)
            myfunction(query)
        else:
            st.write("Please type in a query first :)")
    else:
        pass

if choose == "Contact":
    st.title("Contact Information")
    linkedin = "https://www.linkedin.com/in/maxwell-knowles/"
    st.write("[LinkedIn](%s)" % linkedin)
    spotify = "https://open.spotify.com/artist/2p2YiVrDP0scQefeefDqCO?si=LIyTgWg5T1KL7Fn79lXHPw"
    st.write("[Spotify](%s)" % spotify)
    st.write("Email: maxknowles27@gmail.com")
