Import-Module ActiveDirectory

$Domain="@minstroy.nobl"
$UserOu="OU=Users,DC=minstroy,DC=nobl"
$NewUsersList=Import-CSV "C:\Users\Администратор\Desktop\1.2AD.csv" -Delimiter ";"

ForEach ($User in $NewUsersList) {
    $FullName=$User.FullName
    $Company=$User.company
    $Department=$User.department
    $givenName=$User.givenName
    $title=$User.title
    $City=$User.City
    $telephoneNumber=$User.telephoneNumber
    $sAMAccountName=$User.sAMAccountName
    $sn=$User.sn
    $userPrincipalName=$User.sAMAccountName+$Domain
    $userPassword='QW!@er13'
New-ADUser -PassThru -Path $UserOu -Enabled $True -ChangePasswordAtLogon $True -AccountPassword $userPassword -CannotChangePassword $False -City $City -Company $Company -Department $Department -title $title -OfficePhone $telephoneNumber -DisplayName $FullName -GivenName $givenName -Name $FullName -SamAccountName $sAMAccountName -Surname $sn -UserPrincipalName $userPrincipalName

}