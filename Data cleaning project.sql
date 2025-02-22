

----------------------------------------------------------------------------------------------------------
--Cleaning Data is 50% Quries

select *
from PortfolioProject..Nashvillehousing;

-------------------------------------------------------------------------------------------------------

--Standardize Data format

Select Saledateconverted,convert(date,saledate)
from PortfolioProject..Nashvillehousing;

update PortfolioProject..Nashvillehousing 
SET saledate = CONVERT(date,saledate);

Alter table PortfolioProject..Nashvillehousing 
add Saledateconverted Date;

Update PortfolioProject..Nashvillehousing 
SET Saledateconverted = CONVERT(date,saledate);

------------------------------------------------------------------------------------------------------

--populate property address data

Select *
from PortfolioProject..Nashvillehousing
--where PropertyAddress is null;
order by ParcelID;


Select a.ParcelID,a.PropertyAddress,b.ParcelID,b.PropertyAddress, ISNULL (a.propertyAddress,b.PropertyAddress)
from PortfolioProject..Nashvillehousing a
join PortfolioProject..Nashvillehousing b
     on a.parcelID= b.parcelId
	 and a.[UniqueID ]!= b.[UniqueID ]
where a.PropertyAddress is null;


update a
SET PropertyAddress = ISNULL (a.propertyAddress,b.PropertyAddress)
from PortfolioProject..Nashvillehousing a
join PortfolioProject..Nashvillehousing b
     on a.parcelID= b.parcelId
	 and a.[UniqueID ]!= b.[UniqueID ]
where a.PropertyAddress is null;

------------------------------------------------------------------------------------------------------------
---- Creating out Address into indivdual columns(Address, City, State)

select propertyaddress
from PortfolioProject..Nashvillehousing;

select 
SUBSTRING(propertyaddress,1, CHARINDEX(',',PropertyAddress)-1) as Address,
SUBSTRING(propertyaddress, CHARINDEX(',',PropertyAddress)+1,LEN(propertyaddress)) as Address
from PortfolioProject..Nashvillehousing;

Alter table PortfolioProject..Nashvillehousing 
add PropertySplitAddress nvarchar(225);

Update PortfolioProject..Nashvillehousing 
SET PropertySplitAddress = SUBSTRING(propertyaddress,1, CHARINDEX(',',PropertyAddress)-1);

Alter table PortfolioProject..Nashvillehousing 
add PropertySplitCity nvarchar(225);

Update PortfolioProject..Nashvillehousing 
SET PropertySplitCity = SUBSTRING(propertyaddress, CHARINDEX(',',PropertyAddress)+1,LEN(propertyaddress));

select*
from PortfolioProject..Nashvillehousing;

select OwnerAddress
from PortfolioProject..Nashvillehousing;

select
PARSENAME(Replace(OwnerAddress,',','.') , 3)
,PARSENAME(Replace(OwnerAddress,',','.') , 2)
,PARSENAME(Replace(OwnerAddress,',','.') , 1)
from PortfolioProject..Nashvillehousing;

Alter table PortfolioProject..Nashvillehousing 
add OwnerSplitAddress nvarchar(225);

Update PortfolioProject..Nashvillehousing 
SET OwnerSplitAddress = PARSENAME(Replace(OwnerAddress,',','.') , 3);

Alter table PortfolioProject..Nashvillehousing 
add OwnerSplitCity nvarchar(225);

Update PortfolioProject..Nashvillehousing 
SET OwnerSplitCity = PARSENAME(Replace(OwnerAddress,',','.') , 2);

Alter table PortfolioProject..Nashvillehousing 
add OwnerSplitState nvarchar(225);

Update PortfolioProject..Nashvillehousing 
SET OwnerSplitState = PARSENAME(Replace(OwnerAddress,',','.') , 1);


select*
from PortfolioProject..Nashvillehousing;

---------------------------------------------------------------------------------------------------------------------

--Change Y and N to yes and No in "Sold as Vacant " field

select Distinct(SoldAsVacant),count(SoldAsVacant)
from PortfolioProject..Nashvillehousing
Group by SoldAsVacant
Order by 2;


select SoldAsVacant,
   CASE when SoldAsVacant ='Y' then 'Yes'
        When SoldAsVacant ='N' THEN 'No'
		Else SoldAsVacant
		END
From PortfolioProject..Nashvillehousing;

update PortfolioProject..Nashvillehousing
Set SoldAsVacant= CASE when SoldAsVacant ='Y' then 'Yes'
        When SoldAsVacant ='N' THEN 'No'
		Else SoldAsVacant
		END;

-------------------------------------------------------------------------------------------------------------------

--Remove Duplicates

with RowNumCET as (
select *,
     ROW_NUMBER() OVER(
	 Partition By ParcelId,
	              PropertyAddress,
				  SalePrice,
				  SaleDate,
				  LegalReference
				  Order by
				        UniqueID
						) row_num

From PortfolioProject..Nashvillehousing
--order by ParcelID;
)
select*
from RowNumCET
where row_num>1
order by PropertyAddress;

select *
From PortfolioProject..Nashvillehousing;


-------------------------------------------------------------------------------------------------------
--Delete Unused Colunms

Select*
From PortfolioProject..Nashvillehousing

alter table PortfolioProject..Nashvillehousing
drop column OwnerAddress,TaxDistrict,PropertyAddress


alter table PortfolioProject..Nashvillehousing
drop column SaleDate

-----------------------------------------------------------------------------------------------------