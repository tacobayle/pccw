'''
python3 pccwReadPort.py
List of ports and services associated:
        dataCenterFacility username: equinix-fr5
        name: Eurovision 10G FR5 Port
        speed: 10000 Mbps
        status ACTIVE
        linkState UP
        id: 5e429ef0d6b9a000166c3b65
        capacity total: 10000
        capacity utilised: 200
        capacity remaining: 9800
        List of services:
                name: AWS Direct Connect
                id: 5e5524e032b9d7001625e322
                speed: 100
                status: DELETING
                --
                name: Azure ExpressRoute
                id: 5e7a2b1903be0d0014960141
                speed: 50
                status: ACTIVE
                --
                name: Azure ExpressRoute Primary 1
                id: 5e7a2b1903be0d0014960142
                speed: 50
                status: ACTIVE
                --
                name: Azure ExpressRoute Secondary 1
                id: 5e7a2b1903be0d0014960143
                speed: 50
                status: ACTIVE
                --
        ----
        dataCenterFacility username: telehouse-tfm1-17
        name: Eurovision 10G THN Port
        speed: 10000 Mbps
        status ACTIVE
        linkState UP
        id: 5e46ad092729470016bb2e14
        capacity total: 10000
        capacity utilised: 0
        capacity remaining: 10000
        ----
'''
=========
'''
python3 pccwReadConnection.py 5e7a2b1903be0d0014960143
activeChangedAt: '2020-03-24T15:56:20.145Z'
addonIds: []
alertUtilization: null
alertUtilizationThresholdUserIds: null
billingType: BESPOKE
cdrBillingType: REGIONAL
classOfService: BRONZE
createdAt: '2020-03-24T15:45:29.717Z'
deleted: false
deletedAt: null
destCompany:
  __v: 3
  avatar: null
  avatarId: 5b2000f59308300018e194a2
  background: null
  capabilities:
    layer2: true
    layer2Metros: [9d242983f7a504eebb3eb478, 906681faf944cb387f682ae8, 823bf0527b3f4aec2842fa7d,
      ab0406b767633e395b2cdef4, 6759876168035b17665db6ab]
    layer2Regions: [5a80c7be1347a30012dd1c55, 5a80c7421347a30012dd1c52, 5a80c78c1347a30012dd1c53]
    layer3: false
    layer3Metros: []
    layer3Regions: []
  companies: []
  company:
    address: null
    addresses:
    - address: 5000 148th Ave NE
      city: Redmond
      country: US
      email: null
      geo:
        coordinates: []
        type: Point
      phone: null
      registered: false
      state: WA
      zip: null
    businessRegistrationCertReference: null
    businessRegistrationCertRejectedReason: null
    businessRegistrationCertUploadedAt: null
    businessRegistrationCertVerified: UNVERIFIED
    businessType: Cloud Partner
    city: null
    clientId: null
    companySize: null
    dateFounded: null
    emailDomains: ['@microsoft.com']
    fax: null
    first: null
    industry: null
    last: null
    parentIds: []
    phone: null
    privacy:
      community:
        blackListIds: []
        mode: PUBLIC
        whiteListIds: []
      network:
        blackListIds: []
        mode: PUBLIC
        whiteListIds: []
    regionalInternetRegistry: []
    registeredName: null
    state: null
    website: https://azure.microsoft.com
    zip: null
  createdAt: '2018-06-08T02:33:31.537Z'
  deleted: false
  deletedAt: null
  directConnectPartner: {type: AZURE, verified: true}
  displayOrder: -299
  groups: []
  headline: Your vision.  Your cloud.
  id: 5b19eafb3c835a00180058ab
  isSupport: false
  legalEntityId: null
  location: null
  name: Microsoft Azure
  online: false
  optIntoMarketingEmail: false
  phone: null
  popIds: []
  stats: {articles: 0, events: 0, followers: 28, following: 0, interconnections: 0,
    members: 0, posts: 0, privateArticles: 0, privateEvents: 0, privatePosts: 0}
  status: ACTIVE
  summary: "Microsoft Azure is an ever-expanding set of cloud services to help your\
    \ organization meet your business challenges. It\u2019s the freedom to build,\
    \ manage, and deploy applications on a massive, global network using your favorite\
    \ tools and frameworks."
  system: {welcomeMessage: true}
  tags: []
  type: COMPANY
  updatedAt: '2020-03-24T15:56:30.896Z'
  username: azure
  verified: false
destCompanyId: 5b19eafb3c835a00180058ab
destConfigTag: SERVICE
destControllerId: null
destPort:
  accessCircuit: null
  activeChangedAt: '2018-11-19T06:12:47.070Z'
  billingId: null
  capabilities: {model6Limit: false, model6LimitNumber: null}
  companyId: 5b19eafb3c835a00180058ab
  cosMapping: {BRONZE: null, GOLD: null, SILVER: null, SILVERPLUS: null}
  cosTransparency: null
  createdAt: '2018-08-28T20:36:58.797Z'
  dataCenterFacilityId: 5a9739ccfae7ba00134d378b
  dcpCompanyId: null
  deleted: false
  deletedAt: '1970-01-01T00:00:00.000Z'
  firstActiveAt: null
  iciLink: A
  id: 5b85b26a9939be0014b63891
  importedAt: null
  importer: null
  ip: {ipv4: null, ipv6: null}
  linkState: UP
  linkStateSyncedAt: '2018-11-19T06:12:47.057Z'
  linkStateUpSince: null
  locationId: null
  mediaType: SMF
  metroId: 906681faf944cb387f682ae8
  name: PCCW-LON31-06GMR-CIS-2-SEC-A
  onboarded: null
  onboardedAllocatedBandwidth: null
  onboardedAt: null
  onboardedBy: null
  onboardedDeviceName: null
  onboardedInterfaceName: null
  onboardedStatus: AWAITING_PROCESSING
  onboardedStatusDetail: null
  partner:
    connectionSpeeds:
    - {type: AUTOMATIC, value: 50}
    - {type: AUTOMATIC, value: 100}
    - {type: AUTOMATIC, value: 200}
    - {type: AUTOMATIC, value: 500}
    - {type: AUTOMATIC, value: 1000}
    partnerPort: PCCW-LON31-06GMR-CIS-2-SEC-A
    regionName: null
    regionNames: [UK South]
    type: AZURE
    vlanId: null
    zone: null
  payg: false
  paymentType: plan
  popId: null
  salesRecordId: null
  singleService: false
  speed: 10000
  speedOverprovisioningFactor: 1
  status: ACTIVE
  supportedServices: null
  type: DCP
  updatedAt: '2019-07-25T01:31:39.951Z'
  vlanRanges: []
destPortId: 5b85b26a9939be0014b63891
destPorts:
- accessCircuit: null
  activeChangedAt: '2018-11-19T06:12:41.866Z'
  billingId: null
  capabilities: {model6Limit: false, model6LimitNumber: null}
  companyId: 5b19eafb3c835a00180058ab
  cosMapping: {BRONZE: null, GOLD: null, SILVER: null, SILVERPLUS: null}
  cosTransparency: null
  createdAt: '2018-08-28T20:34:22.605Z'
  dataCenterFacilityId: 5a9739ccfae7ba00134d378b
  dcpCompanyId: null
  deleted: false
  deletedAt: '1970-01-01T00:00:00.000Z'
  firstActiveAt: null
  iciLink: A
  id: 5b85b1cee0fe090014985071
  importedAt: null
  importer: null
  ip: {ipv4: null, ipv6: null}
  linkState: UP
  linkStateSyncedAt: '2018-11-19T06:12:41.851Z'
  linkStateUpSince: null
  locationId: null
  mediaType: SMF
  metroId: 906681faf944cb387f682ae8
  name: PCCW-LON31-06GMR-CIS-1-PRI-A
  onboarded: null
  onboardedAllocatedBandwidth: null
  onboardedAt: null
  onboardedBy: null
  onboardedDeviceName: null
  onboardedInterfaceName: null
  onboardedStatus: AWAITING_PROCESSING
  onboardedStatusDetail: null
  partner:
    connectionSpeeds:
    - {type: AUTOMATIC, value: 50}
    - {type: AUTOMATIC, value: 100}
    - {type: AUTOMATIC, value: 200}
    - {type: AUTOMATIC, value: 500}
    - {type: AUTOMATIC, value: 1000}
    partnerPort: PCCW-LON31-06GMR-CIS-1-PRI-A
    regionName: null
    regionNames: [UK South]
    type: AZURE
    vlanId: null
    zone: null
  payg: false
  paymentType: plan
  popId: null
  salesRecordId: null
  singleService: false
  speed: 10000
  speedOverprovisioningFactor: 1
  status: ACTIVE
  supportedServices: null
  type: DCP
  updatedAt: '2019-07-25T01:36:15.098Z'
  vlanRanges: []
- accessCircuit: null
  activeChangedAt: '2018-11-19T06:12:47.070Z'
  billingId: null
  capabilities: {model6Limit: false, model6LimitNumber: null}
  companyId: 5b19eafb3c835a00180058ab
  cosMapping: {BRONZE: null, GOLD: null, SILVER: null, SILVERPLUS: null}
  cosTransparency: null
  createdAt: '2018-08-28T20:36:58.797Z'
  dataCenterFacilityId: 5a9739ccfae7ba00134d378b
  dcpCompanyId: null
  deleted: false
  deletedAt: '1970-01-01T00:00:00.000Z'
  firstActiveAt: null
  iciLink: A
  id: 5b85b26a9939be0014b63891
  importedAt: null
  importer: null
  ip: {ipv4: null, ipv6: null}
  linkState: UP
  linkStateSyncedAt: '2018-11-19T06:12:47.057Z'
  linkStateUpSince: null
  locationId: null
  mediaType: SMF
  metroId: 906681faf944cb387f682ae8
  name: PCCW-LON31-06GMR-CIS-2-SEC-A
  onboarded: null
  onboardedAllocatedBandwidth: null
  onboardedAt: null
  onboardedBy: null
  onboardedDeviceName: null
  onboardedInterfaceName: null
  onboardedStatus: AWAITING_PROCESSING
  onboardedStatusDetail: null
  partner:
    connectionSpeeds:
    - {type: AUTOMATIC, value: 50}
    - {type: AUTOMATIC, value: 100}
    - {type: AUTOMATIC, value: 200}
    - {type: AUTOMATIC, value: 500}
    - {type: AUTOMATIC, value: 1000}
    partnerPort: PCCW-LON31-06GMR-CIS-2-SEC-A
    regionName: null
    regionNames: [UK South]
    type: AZURE
    vlanId: null
    zone: null
  payg: false
  paymentType: plan
  popId: null
  salesRecordId: null
  singleService: false
  speed: 10000
  speedOverprovisioningFactor: 1
  status: ACTIVE
  supportedServices: null
  type: DCP
  updatedAt: '2019-07-25T01:31:39.951Z'
  vlanRanges: []
destQinQ: true
destRegionId: null
destTag: null
destUntagged: false
destVlan:
  customer:
  - {end: 10, start: 10}
  - {end: 30, start: 30}
  id: null
  service: 8
destVlanRequest: null
duration: null
durationUnit: null
errorReason: null
firstActiveAt: null
id: 5e7a2b1903be0d0014960143
importedAt: null
importer: null
isCreator: true
isReceiver: false
maintenanceMode: false
name: Azure ExpressRoute Secondary 1
parentId: 5e7a2b1903be0d0014960141
partner:
  account: ef0eaba7-1fb5-478f-9fd3-d101e7b385da
  connectionId: null
  crossconnectionStatus: DISABLED
  customerAsnId: null
  destPortIds: [5b85b1cee0fe090014985071, 5b85b26a9939be0014b63891]
  errorMessage: null
  gatewayId: null
  interconnectId: null
  pairingKey: null
  pairingKeys: []
  peering: []
  provisioningStatus: NOTPROVISIONED
  region: null
  secretId: null
  secretKey: null
  speed: 50
  srcPortIds: null
  subtype: NONE
  syncStatus: NONE
  type: AZURE
  vpcId: null
payg: false
paymentTransactionId: null
paymentType: plan
port:
  accessCircuit: null
  activeChangedAt: '2020-02-11T12:32:55.255Z'
  billingId: null
  capabilities: {model6Limit: false, model6LimitNumber: null}
  companyId: 5e3033b5a169240016becc0e
  cosMapping:
    BRONZE: []
    GOLD: []
    SILVER: []
    SILVERPLUS: []
  cosTransparency: null
  createdAt: '2020-02-11T12:32:48.823Z'
  dataCenterFacilityId: 5a9798f0339bad0012edd096
  dcpCompanyId: null
  deleted: false
  deletedAt: null
  firstActiveAt: '2020-02-11T12:32:55.170Z'
  iciLink: A
  id: 5e429ef0d6b9a000166c3b65
  importedAt: null
  importer: null
  ip: {ipv4: null, ipv6: null}
  linkState: UP
  linkStateSyncedAt: '2020-02-11T12:32:55.155Z'
  linkStateUpSince: null
  locationId: null
  mediaType: SMF
  metroId: 27a9a3d2723817f91597b7ba
  name: Eurovision 10G FR5 Port
  onboarded: null
  onboardedAllocatedBandwidth: null
  onboardedAt: null
  onboardedBy: null
  onboardedDeviceName: null
  onboardedInterfaceName: null
  onboardedStatus: AWAITING_PROCESSING
  onboardedStatusDetail: null
  partner:
    connectionSpeeds: []
    type: NONE
  payg: false
  paymentType: plan
  popId: 6934715a-aa21-40fe-ac68-feb657405877
  salesRecordId: '164319'
  singleService: false
  speed: 10000
  speedOverprovisioningFactor: 1
  status: ACTIVE
  supportedServices: []
  tags: []
  type: PHYSICAL
  updatedAt: '2020-02-11T12:32:48.823Z'
  vlanRanges: []
request: {destApproval: null, destMetroId: null, read: false, speed: null, srcApproval: 5e6a0b313f606d001620fb1c,
  status: null, updatedAt: null}
salesRecordId: null
scheduled: false
scheduledTaskList: []
speed: {name: 50 Mbps, value: 50}
srcCompany:
  __v: 2
  avatar: null
  avatarId: null
  background: null
  capabilities:
    layer2: true
    layer2Metros: [27a9a3d2723817f91597b7ba, 906681faf944cb387f682ae8]
    layer2Regions: [5a80c78c1347a30012dd1c53]
    layer3: false
    layer3Metros: []
    layer3Regions: []
  companies: []
  company:
    address: null
    addresses:
    - address: 17A L'ancienne route
      city: Grand Saconnex
      country: CH
      email: null
      geo:
        coordinates: []
        type: Point
      phone: null
      registered: true
      state: null
      zip: '1218'
    businessRegistrationCertReference: null
    businessRegistrationCertRejectedReason: null
    businessRegistrationCertUploadedAt: null
    businessRegistrationCertVerified: UNVERIFIED
    businessType: Enterprise
    city: null
    clientId: null
    companySize: null
    dateFounded: null
    emailDomains: [eurovision.net]
    fax: null
    first: null
    industry: null
    last: null
    parentIds: []
    phone: null
    privacy:
      community:
        blackListIds: []
        mode: PUBLIC
        whiteListIds: []
      network:
        blackListIds: []
        mode: PUBLIC
        whiteListIds: []
    regionalInternetRegistry: []
    registeredName: Eurovision Services SA
    state: null
    website: www.eurovision.net
    zip: null
  createdAt: '2020-01-28T13:14:29.687Z'
  deleted: false
  deletedAt: null
  displayOrder: -299
  groups: []
  headline: null
  id: 5e3033b5a169240016becc0e
  isSupport: false
  legalEntityId: null
  location: null
  name: Eurovision Services
  officeAddress: null
  online: false
  optIntoMarketingEmail: false
  phone: null
  popIds: []
  stats: {articles: 0, events: 0, followers: 3, following: 2, interconnections: 0,
    members: 3, posts: 0, privateArticles: 0, privateEvents: 0, privatePosts: 0}
  status: ACTIVE
  summary: null
  system: {welcomeMessage: true}
  tags: []
  type: COMPANY
  updatedAt: '2020-03-24T17:34:06.185Z'
  username: eurovisionservices
  verified: true
srcCompanyId: 5e3033b5a169240016becc0e
srcConfigTag: CUSTOMER
srcControllerId: null
srcPortId: 5e429ef0d6b9a000166c3b65
srcPorts: []
srcQinQ: true
srcRegionId: null
srcTag: null
srcUntagged: false
srcVlan:
  customer:
  - {end: 3607, start: 3607}
  - {end: 3608, start: 3608}
  id: null
  service: null
srcVlanRequest: null
status: ACTIVE
statusChangedAt: '2020-03-24T15:56:20.145Z'
subconnectionIds:
  primary: []
  secondary: []
subconnections: []
tag: null
type: LAYER2
typeFriendly: Azure ExpressRoute
updatedAt: '2020-03-24T15:56:20.149Z'
version: '2'
'''
