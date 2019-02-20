from fifa_py import get_json, api_scrape
from datetime import datetime

TODAY = datetime.today()

# import information for all countries
from constants import COUNTRY

class League:
    '''

    Input:
    Output:
    '''

    def __init__(self, 
                country, 
                league_id,
                **kwargs):
                
        self.country = country
        self.league_id = league_id



<tr>
    <th scope="row" class="left " data-stat="country" >
        <a href="/en/squads/country/ATG/Antigua-and-Barbuda-Football-Clubs">Antigua and Barbuda Football Clubs</a>
    </th>
    <td class="right iz" data-stat="flag">
        <span class="f-i f-ag">ag</span> 
    </td>
    <td class="right " data-stat="num_clubs" >1</td>
    <td class="left iz" data-stat="competitions" ></td>
</tr>


<tr>
    <th scope="row" class="left " data-stat="country" >
        <a href="/en/squads/country/ENG/England-Football-Clubs">England Football Clubs</a>
    </th>

    <td class="right iz" data-stat="flag" >
        <span class="f-i f-gb-eng">eng</span> 
    </td>

    <td class="right " data-stat="num_clubs" > 154 </td>

    <td class="left " data-stat="competitions" >
        <a href="/en/comps/9/Premier-League-Seasons">Premier League</a>, 
        <a href="/en/comps/10/EFL-Championship-Seasons">EFL Championship</a>, 
        <a href="/en/comps/15/EFL-League-One-Seasons">EFL League One</a>, 
        <a href="/en/comps/16/EFL-League-Two-Seasons">EFL League Two</a>, 
        <a href="/en/comps/34/National-League-Seasons">National League</a>
    </td>
</tr>


<tr>
    <th scope="row" class="left " data-stat="country" >
        <a href="/en/squads/country/SCO/Scotland-Football-Clubs">Scotland Football Clubs</a>
    </th>

    <td class="right iz" data-stat="flag" >
        <span class="f-i f-gb-sco">sco</span> 
    </td>

    <td class="right " data-stat="num_clubs" >30</td>

    <td class="left " data-stat="competitions" >
        <a href="/en/comps/40/Scottish-Premiership-Seasons">Scottish Premiership</a>, 
        <a href="/en/comps/72/Scottish-Championship-Seasons">Scottish Championship</a>
    </td>
</tr>