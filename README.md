# Formats d'échange Blitz Collection
Blitz Collection permet l'intégration de dossiers selon un format pivot répondant à la norme [json schema](https://json-schema.org/). Ce format sera repris dans la future API Blitz Collection.
# Test de JSON contre un schéma
Le script `validation.py` permet de tester l'ensemble des JSON du dossier `examples` contre le schéma préciser dans le champ `$schema` du JSON. Il est aussi possible d'utiliser les outils décrits dans la [documentation JSON schema](https://json-schema.org/tools?query=&sortBy=name&sortOrder=ascending&groupBy=toolingTypes&licenses=&languages=&drafts=&toolingTypes=&environments=&showObsolete=false#validator)
# Description des principaux objets
## Téléphone ([phone](https://github.com/Blitz-BS/blitzCollection/blob/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/phone.schema.json))
Un téléphone comprend
* Une valeur qui est le numéro de téléphone lui même
* Un booléen qui indique s'il s'agit d'un mobile. Cette information peut être utile pour l'émission de SMS par exemple
* Une description libre du numéro de téléphone
* Une qualification : personnel, professionnel, déprécié (mauvais numéro)
## Email ([email](https://github.com/Blitz-BS/blitzCollection/blob/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/email.schema.json))
Les emails suivent la même logique avec
* Une valeur qui est l'email lui même
* Une description libre
* Une qualification : personnel, profession, déprécié
## Adresse ([address](https://github.com/Blitz-BS/blitzCollection/blob/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/address.schema.json))
Une adresse comprend
* Une rue
* Une ville
* Un code postal
* Un pays (ISO 3166-1)
## Contact ([`contact`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/contact.schema.json))
Un contact est une personne physique avec
* une civilité
* un prénom
* un nom
* une langue (ISO 639-2)
Un contact peut disposer de plusieurs
* adresses ([`address`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/address.schema.json))
* email ([`email`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/address.schema.json))
* numéro de téléphone ([`phone`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/phone.schema.json)).
Un contact dispose d'une référence (`reference`) qui est son identifiant unique dans le référentiel de client et du créancier de la société de recouvrement.
## Compte bancaire ([bankAccount](https://github.com/Blitz-BS/blitzCollection/blob/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/bankAccount.schema.json))
Un compte bancaire comprend
* un IBAN
* un code Swift
* Une domiciliation bancaire
* Un nom de titulaire
* Un code banque
* Un code guichet
* Un numéro de compte
## Personne ([`person`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/person.schema.json))
Une personne est une personne physique ou morale, une administration, une indivision ou tout autre entité susceptible de contracter une dette ou une créance. La catégorie de la personne est définie dans le champ `personCategory`.
Une personne peut avoir des compétences (`ability`) lui permettant d'intervenir dans un dossier par exemple comme commissaire de justice, avocat ou comme tribunal. La personne peut disposer d'un compte bancaire.
Une personne a un nom (`name`) qui pour un personne physique est la concaténation de son prénom et de son nom
Une personne peut avoir plusieurs contacts qui ont un rôle pour cette personne. Par exemple si la personne est une entreprise, un contact peut être le commercial et un autre peut être le président.
Dans le cas le plus simple où une personne est une personne physique celle-ci a un seul contact qui est la personne physique elle-même. Le rôles est un champ libre. 
Une personne peut disposer d'un compte bancaire
Dans le cas où une personne est une entreprise celle-ci dispose d'informations qui sont regroupées dans [`companyInfo`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/companyInfo.schema.json)
Comme pour les contacts, une personne dispose d'une référence (`reference`) qui est sont identifiant unique dans le référentiel de client de la société de recouvrement.
## Informations entreprise ([companyInfo](https://github.com/Blitz-BS/blitzCollection/blob/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/companyInfo.schema.json))
Les informations d'entreprise comprennent
* Un numéro d'immatriculation
* Une adresse principale
* Une adresse de facturation
* Un adresse de siège social
* Un téléphone d'entreprise
* Un email d'entreprise
* Une entreprise parente qui est une personne
* Un lien vers un registre des sociétés
## Débiteur ([`debtor`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/debtor.schema.json))

Le débiteur est une personne ([`person`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/person.schema.json)) débiteur, codébiteur ou caution de la créance. 
En fonction de la situation de la dette, les codébiteurs/cautions peuvent avoir un engagement (`undertaking`) c'est à dire un montant maximal qu'il est susceptible de payer.
Si la dette est conjointe alors tous les codébiteurs doivent avoir un engagement dont la somme est égale à la dette initiale. Sinon, si aucun engagement n'est précisé, les codébiteurs/cautions sont dans une situation de dette solidaire.
## Écriture ([`entry`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/entry.schema.json))
Les écritures sont les écritures comptables du compte client du créancier. 
Les écritures disposent des éléments suivants
* une référence (`reference`) unique comme pour les personnes et les contacts
* un libellé (`label`) de la pièce comme par exemple le numéro de la facture
* une date (`entryDate`) comme par exemple la date de la facture
* un montant (`amount`) comme par exemple le montant TTC de la facture
* une devise (`currencyCode`) qui est par défaut la devise du dossier
Par ailleurs les écritures peuvent être lettrées (`lettering`). Le lettrage permet de grouper les écritures sur une créance ce qui permet de calculer le restant dû sur une créance.
Si une écriture est lettrée la somme des montants lettrés doit être égale au montant de l'écriture. 
Si une écriture n'est pas lettrée elle sera lettrée automatiquement à l'intégration selon la stratégie de lettrage définie dans le contrat. 
Il existe différents types d'écriture
* Créances : facture, avis d'échéance de loyer, avis d'échéance de crédit
* Avoir
* Accessoires
* Paiements : paiements, rejets, remboursement
* Opérations diverses (OD) : erreur, ajustement de change
### Créance ([debt](https://github.com/Blitz-BS/blitzCollection/blob/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/debt.schema.json))
Les créances comprennent
* Un sous type : facture, avis d'échéance de loyer, avis d'échéance de crédit
* Une date d'échéance
* Un montant de TVA
* Un taux d'intérêt en cas de retard de paiement
* Des dates de démarrage et d'arrêt du calcul des intérêts
### Avoir ([creditNote](https://github.com/Blitz-BS/blitzCollection/blob/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/creditNote.schema.json))
Les avoirs ne comprennent aucun champ spécifique
### Accessoire ([incidental](https://github.com/Blitz-BS/blitzCollection/blob/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/incidental.schema.json))
Les frais accessoires comprennent
* Une législation : par défaut il s'agit de la législation française
* Un sous type : le sous type est dans la langue de la législation. intérêts de retard, pénalité de retard, indemnité forfaitaire, dommages et intérêts, dépens, article 700, frais répétibles.
### Paiement ([payment](https://github.com/Blitz-BS/blitzCollection/blob/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/payment.schema.json))
Les paiements comprennent
* Un sous type : paiement, rejet, remboursement
* Un date de paiement
* Un mode de paiement : chèque, cash, carte de crédit, prélèvement, virement
* La référence de la personne émettrice
* La référence de la personne bénéficiaire
### Opération diverse ([adjustment](https://github.com/Blitz-BS/blitzCollection/blob/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/adjustment.schema.json))
Les opérations diverses comprennent
* Un sous type : erreur, ajustement de change
## Dossier ([`folder`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/folder.schema.json))
Un dossier correspond à un extrait de compte client dans la comptabilité du créancier. Le dossier comprend
* Un identifiant du contrat entre la société de recouvrement et son client
* Une référence unique du dossier. Cette référence est unique pour un client et un créancier donné.
* Un créancier. Le créancier est une personne ([`person`](https://github.com/Blitz-BS/blitzCollection/blob/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/examples/person.example.json))
* Des débiteurs.
* Des cautions.
* Des écritures comptables qui peuvent être des créances, des avoirs, des paiements, des accessoires et des opérations diverses.
* Des tiers impliqués dans le dossier. Les tiers sont des personnes (`person`)
* Une devise par défaut du dossier.
Quand les dossiers ([`folders`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/folders.schema.json)) sont envoyés en masse, ils sont regroupés par contrat puis par créancier.
# Exemples

Les fichiers d'exemples permettent d'avoir une idée de la représentation des différents objets. En particulier le fichier [`invoices.folders.exemple.json`](https://github.com/Blitz-BS/blitzCollection/blob/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/examples/invoices.folders.example.json) est un exemple de création de dossiers de factures.