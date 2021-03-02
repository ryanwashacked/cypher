questions = ["Do you provide training to your Personnel on data protection and IT security issues? If so, please provide details."]
questions = questions + ["Is personnel accessing our data subject to NDA?"]
questions = questions + ["Acceptable use policy?"]
questions = questions + ["Formal job descriptions?"]
questions = questions +["Testing, validation and promote-to-production procedures"]
questions = questions +["Please provide details of your back up processes including details of how frequently they are tested."]
questions = questions +["Does your organization’s security program maintain any annual third party security accreditation or certifications such as SSAE-16 SOC2, ISO 27001/27002, BITS, PCI-DSS or others? If so, which one(s)?"]

answers = ["Personnel is adequately qualified and trained for the roles and tasks undertaken. Periodic training for enforcing conformance with corporate policies, legislation or regulation updates or enhancement of skills is enforced by the Management. Training conducted annually and upon regulatory change (e.g. CCPA, GDPR). Training is integral part of the company's Quality and Information Security Management System that is certified with ISO 9001 and ISO 27001."]
answers = answers+["Yes, upon hire."]
answers = answers+["Yes regarding the companys personnel plus for you for using the service please refer to the Terms page."]
answers = answers+["Formal job descriptions and qualifications are maintained for all company’s roles. Descriptions and qualifications are periodically (at most annually) reviewed by the Management."]
answers = answers+["The application utilizes a staging infrastructure that mimics the production system. All changes are first introduced and thoroughly tested on the staging environment before being applied to the production servers. Segregated environments and teams, developers and testers/QA."]
answers = answers+["We perform daily system backups. All data is stored encrypted (SSE AES-256) and span a period of 30 days. We use multiple forms of backups so as to maximize the recovery capabilities and speed. We test our backup process annually as part of our BCDR test. Also we have done restorations from backups due to customer requests - customers who have accidentally deleted data and want the DB restored, so backup & restore is part of the company's operations as well. We do not keep local copies of your data in our premises, all data exclusively backed up in the cloud."]
answers = answers+["We have been certified for ISO 9001 and ISO 27001 and our ISMS is structured accordingly. Regarding PCI-DSS compliance, we do not store credit cards in our systems. In case you invoke payments then you are redirected to a PCI-compliant gateway such as Stripe/Paypal where the users are redirected to purchase a course assuming this option is the preferred one set by your domain administrator; Paypal is PCI-compliant (htt ps://www.paypal.com/us/webapps/mpp/pci-compliant-solution) and Stripe is also PCI Service Provider (Level 1) - https://stripe.com/docs/security /stripe. Also our cloud infrastructure provider (AWS) is heavily certified (incl. ISO 27001, SOC 1,2,3)."]