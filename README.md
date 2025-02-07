# Formats d'échange Blitz Collection
Blitz Collection permet l'intégration de dossiers selon un format pivot répondant à la norme [json schema](https://json-schema.org/). Ce format sera repris dans la future API Blitz Collection.
# Test de JSON contre un schéma
Le script `validation.py` permet de tester l'ensemble des JSON du dossier `examples` contre le schéma préciser dans le champ `$schema` du JSON. Il est aussi possible d'utiliser les outils décrits dans la [documentation JSON schema](https://json-schema.org/tools?query=&sortBy=name&sortOrder=ascending&groupBy=toolingTypes&licenses=&languages=&drafts=&toolingTypes=&environments=&showObsolete=false#validator)
# Description des principaux objets

## Contact ([`contact`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/contact.schema.json))

Un contact est une personne physique avec une civilité, un prénom, un nom, une langue pouvant disposer de plusieurs adresses ([`address`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/address.schema.json)), adresse email ([`email`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/address.schema.json)) ou numéro de téléphone ([`phone`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/phone.schema.json)).
Un contact dispose d'une référence (`reference`) qui est sont identifiant unique dans le référentiel de client de la société de recouvrement.
## Personne ([`person`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/person.schema.json))
Une personne est une personne physique ou morale, une administration, une indivision ou tout autre entité susceptible de contracter une dette ou une créance. Une personne peut avoir des compétences (`ability`) lui permettant d'intervenir dans un dossier par exemple comme commissaire de justice, avocat ou comme tribunal. La personne peut disposer d'un compte bancaire.
Une personne peut avoir plusieurs contacts qui ont un rôle pour cette personne. Par exemple si la personne est une entreprise, un contact peut être le commercial et un autre peut être le président.
Dans le cas le plus simple où une personne est une personne physique celle-ci a un seul contact qui est la personne physique elle-même.
Dans le cas où une personne est une entreprise celle-ci dispose d'information qui sont regroupées dans [`companyInfo`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/companyInfo.schema.json)
Comme pour les contacts, une personne dispose d'une référence (`reference`) qui est sont identifiant unique dans le référentiel de client de la société de recouvrement.
## Debiteur ([`debtor`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/debtor.schema.json))

Le débiteur est le tiers qui débiteur de la créance. C'est une personne (`person`) qui a potentiellement un engagement. Le débiteur peut être le débiteur du créance ou un des codébiteurs ou même une caution de la créance.
En fonction de la situation de la dette, les codébiteurs/cautions peuvent avoir un engagement (`undertaking`). Si la dette est conjoite alors tous les codébiteurs doivent avoir un engagement dont la somme est égal à la dette intiale. Sinon, si aucun engagement n'est précisé, les codébiteurs/cautions sont dans une situation de dette solidaire.
## Créance ([`debt`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/person.schema.json))

Comme pour les personnes et les contacts, une créance dispose d'une référence (`reference`). Une créance s'appuie sur une pièce qui dispose d'un numéro (`label`) et d'une date (`issueDate`). Il s'agit par exemple d'un numéro de facture et la date de la facture.  La créance comporte également un montant TTC (`amount`), un montant de TVA (`vatAmount`) et une date d'exigibilité (`dueDate`). Enfin le solde TTC de la créance (`balance`) et le solde de TVA (`vatBalance`) sont constatés à une date (`balanceDate`) qui en général correspond à la date de transfert des informations. Tous ces montants montants sont constatés dans une monnaie qui est l'euro par défaut.
Des frais accessoires ([`ìncidental`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/incidental.schema.json)) peuvent être attachés à la créance.

  

## Frais accessoires ([`incidental`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/incidental.schema.json))

  

Les frais accessoires sont soit de type frais fixe (`fees`) soit de type intérêts (`interests`). Les frais peuvent être de différentes catégories (`category`) exprimées dans la langue du droit dans lequel s'applique ces frais accessoires. Pour l'instant seuls les frais accessoires français existent à savoir les intérêts de retard, les pénalités de retard, les indemnités forfaitaires, les dommages et intérêts", les dépens, l'article 700. On remarque que certains frais accessoires s'appliquent à la créance ([`debt`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/debt.schema.json)) alors que d'autres d'appliquent au dossier ([`folder`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/folder.schema.json))

  

Dans le cas des frais fixe, ils comprennent uniquement un montant (`amount`) ainsi qu'un nom (`name`) qui est un champ libre.

  

Dans le cas des intérêts, ils comprennent un taux d'intérêt, une date de démarrage des intérêts et éventuellement une date de fin des intérêts.

  

## Dossier ([`folder`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/folder.schema.json))

  

Les dossiers regroupent un ensemble de créances ([`debt`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/person.schema.json)) avec des débiteurs (`debtors`) (un débiteur ou des co-débiteurs) et des cautions (`guarantors`) qui sont tous des débiteurs ([`debtor`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/debtor.schema.json)) qui déterminent la situation de dette/caution (conjointe ou solidaire) avec leurs engagments respectifs.

  

Les dossiers regroupent cet ensemble avec également un créancier et des tiers qui sont tous des personnes ([`person`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/person.schema.json)). Les tiers regroupent les intervenants périphériques au dossier comme les commissaires de justice, les avocats ou les tribunaux.

  

Des frais accessoires ([`incidental`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/incidental.schema.json)) peuvent être attachés au dossier. Il s'agit des frais accessoires judiciaires qui sont les seuls qui peuvent être attaché au dossier. Le dossier précise également la monnaie dans laquelle les frais accessoires sont libellés.

  

Le dossier est créé dans le cadre d'un contrat (`contractId`) entre la société de recouvrement et son client. Le client peut être le créancier mais peut être également une autre personne.

  

Quand les dossiers ([`folders`](https://raw.githubusercontent.com/Blitz-BS/blitzCollection/refs/heads/MGP-421-modularisation-de-l-objet-json-schema-pour-l-integ/json_schema/folders.schema.json)) sont envoyés en masse, ils sont regroupés par contrat puis par créancier.

  

# Exemples

  

Les fichiers d'exemples permettent d'avoir une idée de la représentation des différents objets. En particulier le fichier `invoices.folders.exemple.json` est un exemple de création de dossiers de factures.