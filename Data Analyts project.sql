
select*
from PortfolioProject..Deaths
where continent is not null
order by 3,4

----select*
----from PortfolioProject..Vaccinations
----order by 3,4

--select data that we are going to be using

select location,date,total_cases,new_cases, total_deaths,population
from PortfolioProject..Deaths
order by 1,2

--Looking at Total Cases vs Total Deaths
--Shows likelihood of dying if you contract covid in your country
SELECT location,
       date,
       total_cases,
       total_deaths,
       (CAST(total_deaths AS FLOAT) / CAST(total_cases AS FLOAT))*100 as DeathPercentages
FROM PortfolioProject..Deaths
where location like '%state%'
and  continent is not null
ORDER BY location, date;

--looking at total cases vs population
--Shows what percentage of population got covid

SELECT location, date,total_cases,population,
       (CAST(total_cases AS FLOAT) / CAST(population AS FLOAT))*100 as PercentPopulationInfacted
FROM PortfolioProject..Deaths
--where location like '%state%'
where continent is not null
ORDER BY location, date;


--Looking at countries with  Highest Infaction Rate compared to population

SELECT location,population,max(total_cases) as HighestInfactionCount,
       max((CAST(total_cases AS FLOAT) / CAST(population AS FLOAT)))*100 as PercentPopulationInfacted
FROM PortfolioProject..Deaths
--where location like '%state%'
Group by location,population
ORDER BY PercentPopulationInfacted desc;

--Showing countries with Highest Death Count  per Population

select location,max(cast(total_deaths as int)) as TotalDeathCount
from PortfolioProject..Deaths
--where location like %state%
where continent is not null
group by location
order by TotalDeathCount desc;

--Let's break things down by continent



--- Showing continent with thevhightest death count per population

select continent,max(cast(total_deaths as int)) as TotalDeathCount
from PortfolioProject..Deaths
--where location like %state%
where continent is not null
group by continent
order by TotalDeathCount desc;

--GLOBAL Numbers

SELECT sum(new_cases) as Total_cases,
       sum(CAST(total_deaths AS BIGINT)) as Total_Deaths,
       sum(CAST(total_deaths AS BIGINT)) / NULLIF(sum(new_cases), 0) * 100 as DeathPercentages
FROM PortfolioProject..Deaths
WHERE continent IS NOT NULL
ORDER BY 1, 2;


--Looking at total population vs vaccinations

select dea.continent,dea.location,dea.date,dea.population,vac.new_vaccinations,
sum(convert(bigint,vac.new_vaccinations)) over (partition by dea.location order by dea.location,dea.date) as rollingpeoplevaccinated
--(rollingpeoplevaccinated/population)*100
from PortfolioProject..Deaths  dea
join PortfolioProject..Vaccinations  vac 
     on dea.location = vac.location
	 and dea.date = vac.date
where dea.continent is not null
order by 2,3;

--USE CTE

with popvsvac (continent, location, date, population, new_vaccination, rollingpeoplevaccinated)
as
(
select dea.continent,dea.location,dea.date,dea.population,vac.new_vaccinations,
sum(convert(bigint,vac.new_vaccinations)) over (partition by dea.location order by dea.location,dea.date) as rollingpeoplevaccinated
--(rollingpeoplevaccinated/population)*100
from PortfolioProject..Deaths  dea
join PortfolioProject..Vaccinations  vac 
     on dea.location = vac.location
	 and dea.date = vac.date
where dea.continent is not null
--order by 2,3;
)

select*, (rollingpeoplevaccinated/population)*100 
from popvsvac;


--TEMP TABLE

create table #PrecentPopulationVaccinated
(
Continent nvarchar(225),
location nvarchar(255),
date datetime,
population numeric,
new_vaccinations numeric,
rollingpeoplevaccinated numeric
)



insert into #PrecentPopulationVaccinated
select dea.continent,dea.location,dea.date,dea.population,vac.new_vaccinations,
sum(convert(bigint,vac.new_vaccinations)) over (partition by dea.location order by dea.location,dea.date) as rollingpeoplevaccinated
--(rollingpeoplevaccinated/population)*100
from PortfolioProject..Deaths  dea
join PortfolioProject..Vaccinations  vac 
     on dea.location = vac.location
	 and dea.date = vac.date
--where dea.continent is not null
--order by 2,3;

select*, (rollingpeoplevaccinated/population)*100 
from #PrecentPopulationVaccinated;


--Creating view to store data for later visualizations


Create View PrecentPopulationVaccinated1 as
select dea.continent,dea.location,dea.date,dea.population,vac.new_vaccinations,
sum(convert(bigint,vac.new_vaccinations)) over (partition by dea.location order by dea.location,dea.date) as rollingpeoplevaccinated
--(rollingpeoplevaccinated/population)*100
from PortfolioProject..Deaths  dea
join PortfolioProject..Vaccinations  vac 
     on dea.location = vac.location
	 and dea.date = vac.date
where dea.continent is not null
--order by 2,3;

select * from PrecentPopulationVaccinated1;


