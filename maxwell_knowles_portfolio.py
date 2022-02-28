## Imports
import urllib
import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import urllib.request

with st.sidebar:
    choose = option_menu("Maxwell's Portfolio", ["Bio & Resume", "Prototypes & Tools", "Consulting with Eikona", "Contact"],
                         icons=['house', 'arrow-clockwise', 'activity', 'archive'],
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
    col_photo, col_about = st.columns(2)
    with col_about:
        st.header('About')
        st.write("I completed my undergraduate studies as an Edward J. Sexton Fellow of Philosophy, Politics, and Economics at Claremont McKenna College in 2020 before joining Zero as its eighth full-time team member. Since starting in May of 2020, I've focused on elevating Zero's tech and data visibility, collaborating regularly with engineering, data science, warehouse and fleet operations, growth, and business operations. I'm currently taking coursework in entrepreneurship and venture capital at Claremont Graduate University and competing in the javelin throw, continuing to work in Product along the way.")
        st.write("Thanks for taking the time to learn a bit more about me. I invite you to look through this portfolio web app I created with Python and Streamlit.")
    with col_photo:
        st.image("https://github.com/maxwellknowles/portfolio/raw/main/_89A6473_DxO%20.jpg")
    resume = "https://github.com/maxwellknowles/portfolio/raw/main/Maxwell_Knowles_Resume_2022.pdf"
    st.write("[Download Resume](%s)" % resume)
    with st.expander("See Resume"):
            st.image("https://github.com/maxwellknowles/portfolio/raw/main/resume.png")

    st.header('Work Experience')
    st.subheader("Zero Grocery")
    st.markdown("**Product Manager** _(August 2021 - Present)_")
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
    st.subheader("Claremont McKenna College")
    st.markdown("**BA in Philosophy, Politics, and Economics** _(December 2020)_")
    with st.expander("Senior Thesis"):
        thesis = "https://scholarship.claremont.edu/cmc_theses/2502/"
        st.write("[_Populism: An Exploration into the American Case Through the Academic Literature, Data Analysis, and Fiction_](%s)" % thesis)
        st.write("The twenty-first century has seen a rise in populist leadership and rhetoric throughout the globe, with the United States standing as one powerful case. This thesis hopes to develop the “story” of populism from multiple perspectives, attempting to not only inform but change the way we approach the populist movement in America, and perhaps, the world. In Part I, I summarize and blend much of the core literature written on populism and economic change, developing the story that populism in America today has its roots in the significant techno-economic and cultural paradigmatic shifts of the 1970s. Social media and an evolving political philosophy, particularly among the youth, are also explored. In Part II, I iterate multiple predictive data models using roughly 20 dimensions of democratic and economic life in the United States as independent variables, with different definitions of populism as the dependent variable. I find — counter to what the aforementioned literature might imply — that increasing unemployment is negatively correlated with populist leadership (at a significance level of 0.05, no less), while the “civil society organization participatory environment” and “social class equality in civil liberty” variables are positively correlated, corresponding conceptually with the literature. Finally, Part III is a creative work — The Mind of Demos — in which a fictional college student allegorizes the rise and nature of populism in six cantos, complete with two fictional commentaries and a forward by a fictional professor from the future.")
    with st.expander("Selected coursework"):
        st.write("The Politics of the Gig Economy, Data Science & Statistical Learning, The Idea of Poetry, 7 Steps to Startup, Entrepreneurial Finance, Startup Business Models")

    st.header("Athletics") 
    st.subheader("CMS Track & Field")
    st.markdown("**Javelin Thrower** _(January 2017 - Present)_")
    with st.expander("See details"):
        st.write("• Returned to Claremont for the 2022 season to compete with final year of NCAA athletic eligibility, ranked #4 in school history in the javelin throw")
        st.write("• Voted Men’s Team Captain and nominated for CMS Junior Athlete of the Year in 2019")
        st.write("• SCIAC Champion (2019), USTFCCCA All-West Region honoree (2019), USTFCCCA All-Academic (2019), and NCAA Qualifier, ranking 12th in DIII nationally in 2019")

    st.header("Music") 
    st.markdown("**Singer-Songwriter & Producer** _(November 2020 - Present)_")
    st.write("Write and record indie-alternative music, both instrumental and vocal :)")
    spotify = "https://open.spotify.com/artist/2p2YiVrDP0scQefeefDqCO?si=b7X6T-Y1Q6eG6DwsPTKbyg"
    st.write("[Visit my Spotify!](%s)" % spotify)

if choose == "Data-Intensive Work":
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
    

if choose == "Prototypes & Tools":
    st.title("Prototypes & Tools")
    st.write("During my time working in Product at Zero Grocery (an early-stage startup), I quickly learned the value of being able to rapidly spin up low or no-code solutions for ad hoc and isolated issues in order to keep our lean team of software engineers on our established roadmap. Engineering at a startup is often a precious resource, and I have embraced the challenge of both becoming a more technical PM and utilizing low-code resources — such as Streamlit and Glide Apps — to solve business problems.")

    st.header("Tool: Stock Verification")
    with st.expander("See details"):
        st.subheader("Purpose")
        st.write("Allow operations and merchandising leads to verify stock levels for items marked out-of-stock as pickers fulfill orders.")
        st.subheader("How It Works")
        st.write("I wrote a Python script that filtered orders on their packing status, checked each item in each relevant order for a 'not_packaged' attribute, then uploaded a dataframe of out-of-stock items in in-progress orders to Google Sheets. I deployed the script in GCP, then used the Google Cloud Scheduler to automate running the script every 5 minutes, allowing our team to adapt in real-time. Finally, I used one of my favorite no-code solutions, Glide Apps, to create an easy mobile UI for teammates to find and sort the relevant data. Glide treats spreadsheets like a database, so as long my GCP function continued to update the data in Google Sheets, app users would have a constant flow of accurate and actionable information.")
        st.subheader("Screen Recorded Walkthrough")
        st.video("https://youtu.be/NEJvjzBdl9k")
        glide = "www.glideapps.com"
        st.caption("Find more information on Glide [here](%s)" % glide)
    st.header("Tool: Zero Grocery Analytics Streamlit Web App")
    with st.expander("See details"):
        st.subheader("Purpose")
        st.write("To create the most comprehensive place for different teams to come and engage with data from three Shopify sites and inFlow.")
        st.subheader("How It Works")
        st.write("I wrote a Python script that pulled in data from spreadsheets (which were populated with GCP functions that interacted with Shopify and inFlow at set intervals, preventing us from hitting API call limits). I then used the Streamlit library to present this data in a user-friendly manner, organizing the data thematically and implementing charts, maps, rankings, and k-means clustering.")
        st.subheader("Screen Recording")
        st.video("https://youtu.be/vn3SJHaw4tM")

#if choose == "Product & Feature Examples":
#   st.title("Product & Feature Examples")
#    st.header("Implementing Delivery Windows: An Early & Adaptable Solution at Zero Grocery")
#    st.subheader("")
#    st.write("To create the most comprehensive place for different teams to come and engage with data from three Shopify sites and inFlow.")
#    st.subheader("Product Considerations")
#    st.write("To create the most comprehensive place for different teams to come and engage with data from three Shopify sites and inFlow.")
#    st.subheader("Tackling the Problem")
#    st.write("To create the most comprehensive place for different teams to come and engage with data from three Shopify sites and inFlow.")

#    st.header("The Picker App: A Solution for Zero")

if choose == "Consulting with Eikona":
    st.title("Consulting with Eikona")
    eikona_link = "eikona.art"
    eikona_streamlit_app = "https://share.streamlit.io/maxwellknowles/eikona/main/eikona_projection.py"
    st.write("Eikona — [a startup](%s) working at the nexus of gaming and NFTs — is currently preparing to pitch to angel investors. I've served as a product and strategy consultant on the project, with this Streamlit app serving as one tool in developing and visualizing Eikona's financial projections." % eikona_link)
    st.write("You can see the live Streamlit app for Eikona [here](%s)." % eikona_streamlit_app)

    #data
    coinbase_users = pd.read_csv("https://raw.githubusercontent.com/maxwellknowles/eikona/main/coinbase_users.csv")
    pokemongo_users = pd.read_csv("https://raw.githubusercontent.com/maxwellknowles/eikona/main/pg_users.csv")

    st.title('Eikona Model')
    st.header('Early Prototype')

    col1, col2 = st.columns(2)

    with col1:
        cb_historic_rate = ((coinbase_users['Coinbase Users'][len(coinbase_users)-1]-coinbase_users['Coinbase Users'][0])/coinbase_users['Coinbase Users'][0])/8
        cb_historic_rate = str(round(cb_historic_rate*100))+" %"
        st.write('Coinbase Average Annual User Growth (2014-2021):', cb_historic_rate)
        cb_growth = st.slider('Estimated YoY Growth (%) for Coinbase Users from 2022 Onward...', -100, 1000, 100)
        cb_growth = cb_growth*0.01
        l = []
        for i in range(1,5):
            year = str(2021+i)
            cb_users = round(56*(1+cb_growth)**i)
            tup=(year, cb_users)
            l.append(tup)
        cb_projected = pd.DataFrame(l, columns=['Year','Coinbase Users'])
        coinbase_users = coinbase_users.append(cb_projected, ignore_index=True)
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

    with col2:
        pg_historic_rate = ((pokemongo_users['PG Users'][len(pokemongo_users)-1]-pokemongo_users['PG Users'][1])/pokemongo_users['PG Users'][1])/4
        pg_historic_rate = str(round(pg_historic_rate*100))+" %"
        st.write('Pokemon Go Average Annual User Growth (2017-2020):', pg_historic_rate)
        pg_growth = st.slider('Estimated YoY Growth (%) for Pokemon Go Users from 2021 Onward...', -100, 1000, 40)
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
        
        st.subheader('Pokemon Go Users (in millions)')
        st.line_chart(pokemongo_users)

    #st.subheader('Estimated Users in NFT Space')

    st.header('Eikona Financial Projections: Early and Terminal')
    st.subheader('Eikona early projections, starting with an estimated 1000 core users by end of 2022...')
    col3, col4 = st.columns(2)
    with col3:
        eikona_growth = st.slider('Estimate YoY Growth (%) for Eikona Users from 2023 to 2025', 0, 1000, 500)
        eikona_growth = eikona_growth*0.01
        l = []
        for i in range(0,4):
            year = datetime.strptime(str(2022+i),"%Y")
            eikona_users = 1000*(1+eikona_growth)**i
            tup=(year, eikona_users)
            l.append(tup)
        eikona_projected = pd.DataFrame(l, columns=['Year','Projected Eikona Users'])
        eikona_projected = eikona_projected.set_index('Year')

        st.subheader('Projected Eikona Users')
        st.line_chart(eikona_projected)

    with col4:
        st.subheader('Toggle Estimates for Revenue and Costs')
        cost_mint = st.slider('Estimated Cost of User to Mint ($)...', 0.00, 5.00, 0.25, 0.25)
        server_cost = st.slider('Estimated Server Costs (Per User in $)...', 0.00, 1.00, 0.10, 0.01)
        price_mint = st.slider('Estimated Price for User to Mint ($)...', 0.00, 10.00, 5.00, 0.25)
        conversion_rate = st.slider('Estimated Share of Users Who Mint (%)...', 0, 100, 50)
        conversion_rate = conversion_rate*0.01
        ar_ad_cpm = st.slider('Estimated Avg Number of Additional Mints (Adventures) Per Converted User', 0, 50, 10)

    eikona_projected = eikona_projected.reset_index()
    l = []
    for i in eikona_projected.iterrows():
        year = i[1]['Year']
        converts = round(i[1]['Projected Eikona Users']*conversion_rate)
        cost = (server_cost*eikona_users)+(cost_mint*converts) + (converts*ar_ad_cpm*cost_mint) + (server_cost*converts*ar_ad_cpm)
        revenue = converts*price_mint + (converts*ar_ad_cpm*price_mint)
        profit = revenue - cost
        #revenue = '${:,}'.format(float(round(converts*price_mint)))
        #profit = '${:,}'.format(float(round(profit)))
        tup=(year,converts, cost, revenue, profit)
        l.append(tup)
    eikona_finances = pd.DataFrame(l, columns=['Year','Converts','Costs', 'Revenue', 'Profit'])

    st.subheader('Early Financial Performance')
    col5, col6 = st.columns(2)
    with col5:
        eikona_finances
    with col6:
        eikona_finances_graph = eikona_finances[['Year','Revenue', 'Costs', 'Profit']]
        eikona_finances_graph = eikona_finances_graph.set_index('Year')
        st.line_chart(eikona_finances_graph)


if choose == "Contact":
    st.title("Contact Information")
    linkedin = "https://www.linkedin.com/in/maxwell-knowles/"
    st.write("[LinkedIn](%s)" % linkedin)
    spotify = "https://open.spotify.com/artist/2p2YiVrDP0scQefeefDqCO?si=LIyTgWg5T1KL7Fn79lXHPw"
    st.write("[Spotify](%s)" % spotify)
    st.write("Email: maxknowles27@gmail.com")
    
