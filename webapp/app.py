from flask import Flask, render_template, request

app = Flask(__name__)




@app.route('/')
def home():
    #obtain get params
    state = request.args.get("state", default=None, type=str)
    #dictionary of states
    states={'AK':'Alaska','AL':'Alabama','AR':'Arkansas','AZ':'Arizona','CA':'California', 
    'CO':'Colorado','CT':'Connecticut','FL':'Florida','GA':'Georgia','IA':'Iowa','ID':'Idaho',
    'IL':'Illinois','IN':'Indiana','KS':'Kansas','KY':'Kentucky','LA':'Louisiana', 'MD':'Maryland',
    'MO':'Missouri','NC':'North Carolina','ND':'North Dakota','NH':'New Hampshire', 'NV':'Nevada', 
    'NY':'New York','OH':'Ohio', 'OK':'Oklahoma','OK (Special)':'Oklahoma Special','PA':'Pennsylvania',
    'SC':'South Carolina','SD': 'South Dakota','WA':'Washington','WI':'Wisconsin','UT':'Utah', 
    'VT':'Vermont'} 



    if state == None:
        return render_template( 'index_all.html', states=states, )
    elif state in states.keys():
        state_full=states[state]
        #dictionaries for candidates
        R={'New Hampshire':'Don Bolduc', 'Alabama':'Katie Britt', 'Maryland':'Chris Chaffee', 'Nevada':'Adam Laxalt', 'Iowa':'Chuck Grassley',
        'Arizona':'Blake Masters for Senate','Pennsylvania':'Dr. Mehmet Oz', 'Missouri':'Eric Schmitt', 'Vermont':'Gerald Malloy for Senate', 
        'Georgia':'Herschel Walker', 'Ohio':'JD Vance', 'Oklahoma':'James Lankford', 'Colorado':"Joe O`Dea for Colorado", 
        'Arkansas':'John Boozman', 'North Dakota':'John Hoeven', 'Louisiana':'John Neely Kennedy', 'South Dakota':'John Thune', 
        'Illinois':'Kathy Salvi', 'Connecticut':'Leora Levy', 'Oklahoma Special':'Markwayne Mullin', 'Kansas': 'Jerry Moran', 
        'Alaska':'Lisa Murkowski', 'New York':'Joe Pinion', 'Florida':'Marco Rubio', 'California':'Mark Meuser for U.S. Senate', 
        'Idaho':'Mike Crapo For U.S. Senate', 'Utah':'Mike Lee', 'Kentucky':'Rand Paul', 'Wisconsin':'Ron Johnson', 
        'North Carolina':'Ted Budd', 'Washington':'Tiffany Smiley', 'South Carolina':'Tim Scott', 'Indiana':'Todd Young'}

        D={"Iowa":'Admiral Mike Franken', 'California':'Alex Padilla', 'South Dakota':'Brian Bengs for U.S. Senate', 
        'Kentucky':'Charles Booker', 'Arizona':'Captain Mark Kelly', 'Nevada':'Catherine Cortez Masto', 'North Carolina':'Cheri Beasley', 
        'Maryland':'Chris Van Hollen', 'New York':'Chuck Schumer D-NY', 'Alabama':'Dr. Will Boyd for Alabama','Utah':'Evan McMullin', 
        'Pennsylvania':'John Fetterman', 'Oklahoma':'Kendra Horn', 'Louisiana':'Luke Mixon for Louisiana', 
        'Oklahoma Special':'Madison Horn - U.S. Senate Candidate', 'New Hampshire':'Maggie Hassan', 'Wisconsin':'Mandela Barnes', 
        'Kansas':'Mark Holland', 'South Carolina': 'Krystle Matthews', 'Colorado':'Michael Bennet', 
        'Arkansas':'Natalie James for Arkansas', 'Washington':'Patty Murray', 'Vermont':'Peter Welch', 
        'Georgia':'Reverend Raphael Warnock', 'Connecticut':'Richard Blumenthal', 'Illinois':'Tammy Duckworth', 'Alaska':'Patricia Chesbro',
        'Indiana':'Thomas McDermott Jr.', 'Missouri':'Trudy Busch Valentine', 'Florida':'Val Demings','North Dakota':'Katrina Christiansen',
        'Idaho':'David Roth', 'Ohio':'Tim Ryan'}

        no_ads=['Katie Britt','Chris Chaffee','Jerry Moran','Joe Pinion','Krystle Matthews','Katrina Christiansen','Patricia Chesbro','David Roth']


        
        return render_template( 'index_state.html', states=states, state_full=state_full, dem_can=D[state_full], rep_can=R[state_full], no_ads=no_ads )
    else:
        return render_template( 'index_error.html', states=states, )

    
@app.route('/about')
def about():
    #dictionary of states
    states={'AK':'Alaska','AL':'Alabama','AR':'Arkansas','AZ':'Arizona','CA':'California', 
    'CO':'Colorado','CT':'Connecticut','FL':'Florida','GA':'Georgia','IA':'Iowa','ID':'Idaho',
    'IL':'Illinois','IN':'Indiana','KS':'Kansas','KY':'Kentucky','LA':'Louisiana', 'MD':'Maryland',
    'MO':'Missouri','NC':'North Carolina','ND':'North Dakota','NH':'New Hampshire', 'NV':'Nevada', 
    'NY':'New York','OH':'Ohio', 'OK':'Oklahoma','OK (Special)':'Oklahoma Special','PA':'Pennsylvania',
    'SC':'South Carolina','SD': 'South Dakota','WA':'Washington','WI':'Wisconsin','UT':'Utah', 
    'VT':'Vermont'} 

    return render_template( 'about.html', states=states )
@app.route('/code')
def code():
    #dictionary of states
    states={'AK':'Alaska','AL':'Alabama','AR':'Arkansas','AZ':'Arizona','CA':'California', 
    'CO':'Colorado','CT':'Connecticut','FL':'Florida','GA':'Georgia','IA':'Iowa','ID':'Idaho',
    'IL':'Illinois','IN':'Indiana','KS':'Kansas','KY':'Kentucky','LA':'Louisiana', 'MD':'Maryland',
    'MO':'Missouri','NC':'North Carolina','ND':'North Dakota','NH':'New Hampshire', 'NV':'Nevada', 
    'NY':'New York','OH':'Ohio', 'OK':'Oklahoma','OK (Special)':'Oklahoma Special','PA':'Pennsylvania',
    'SC':'South Carolina','SD': 'South Dakota','WA':'Washington','WI':'Wisconsin','UT':'Utah', 
    'VT':'Vermont'} 

    return render_template( 'code.html', states=states )
@app.route('/contact')
def contact():
    #dictionary of states
    states={'AK':'Alaska','AL':'Alabama','AR':'Arkansas','AZ':'Arizona','CA':'California', 
    'CO':'Colorado','CT':'Connecticut','FL':'Florida','GA':'Georgia','IA':'Iowa','ID':'Idaho',
    'IL':'Illinois','IN':'Indiana','KS':'Kansas','KY':'Kentucky','LA':'Louisiana', 'MD':'Maryland',
    'MO':'Missouri','NC':'North Carolina','ND':'North Dakota','NH':'New Hampshire', 'NV':'Nevada', 
    'NY':'New York','OH':'Ohio', 'OK':'Oklahoma','OK (Special)':'Oklahoma Special','PA':'Pennsylvania',
    'SC':'South Carolina','SD': 'South Dakota','WA':'Washington','WI':'Wisconsin','UT':'Utah', 
    'VT':'Vermont'} 

    return render_template( 'contact.html', states=states )